import time
import signal
import sys
import requests
import socket
import os
from utils.colors import color_text
from datetime import datetime


def handle_exit(signum, frame):
    print(color_text("\n[!] Scan interrupted. Exiting cleanly...", "red"))
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)


def is_port_open(host, port):
    try:
        with socket.create_connection((host, port), timeout=3):
            return True
    except Exception:
        return False

def scan_paths(base_url, host, protocol, found):
    paths = [
    'admin', 'administrator', 'admin/login', 'admin1', 'admin2', 'adminpanel',
    'adminarea', 'admin.php', 'admin.html', 'admin.aspx', 'admin.jsp',
    'cpanel', 'controlpanel', 'staff', 'staff/login',
    'system/admin', 'backend', 'manage',
    'login', 'login.php', 'login.html', 'index.php', 'signin', 'secure'

    ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive',
        'DNT': '1'
   }

    for path in paths:
        url = f"{protocol}://{host}/{path}"
        try:
            res = requests.get(url, headers=headers, timeout=5, allow_redirects=False)
            if res.status_code in [200, 301, 302]:
                status_label = "FOUND" if res.status_code == 200 else "REDIRECT"
                status_label = "FOUND" if res.status_code == 200 else "REDIRECT"
                found.append(url)
            elif res.status_code == 403:
                print(color_text(f"[FORBIDDEN] {url}", "yellow"))
            else:
                print(color_text(f"[-] {url} (Status: {res.status_code})", "red"))
        except requests.exceptions.RequestException as e:
            print(color_text(f"[ERROR] {url} - {e}", "red"))
        time.sleep(0.2)

def run():
    print(color_text("\n[+] Starting Admin Panel Finder (HTTP + HTTPS)...\n", "cyan"))
    
    raw_input = input("Enter target host (e.g., example.com or 192.000.0.0): ").strip()
    host = raw_input.replace("http://", "").replace("https://", "").split('/')[0]

    found_urls = []

    if is_port_open(host, 80):
        print(color_text(f"\n[+] HTTP (80) open – Scanning http://{host}", "blue"))
        scan_paths("http", host, "http", found_urls)
    else:
        print(color_text(f"[!] Port 80 not open on {host}", "red"))

    if is_port_open(host, 443):
        print(color_text(f"\n[+] HTTPS (443) open – Scanning https://{host}", "blue"))
        scan_paths("https", host, "https", found_urls)
    else:
        print(color_text(f"[!] Port 443 not open on {host}", "red"))

    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join("reports", f"adminfinder_{host.replace('.', '_')}_{timestamp}.txt")

    with open(filename, "w") as f:
        if found_urls:
            for url in found_urls:
                f.write(url + "\n")
            print(color_text(f"\n[+] Results saved to file: {filename}", "cyan"))
        else:
            f.write("No admin panels found.\n")
            print(color_text("\n[-] No admin panels found.", "yellow"))
            print(color_text(f"[+] Results saved to file: {filename}", "cyan"))

