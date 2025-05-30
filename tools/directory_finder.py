import requests
from utils.colors import color_text
from datetime import datetime
import os
import time

def run():
    print(color_text("\n[+] Starting Directory Brute Forcer...\n", "cyan"))
    base_url = input("Enter full target URL (e.g., https://example.com): ").strip().rstrip("/")

    paths = [
        'admin', 'dashboard', 'backup', 'config', 'db', 'uploads', 'images',
        'includes', 'private', 'staging', 'dev', 'logs', '.git'
    ]

    found = []
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_name = base_url.replace("https://", "").replace("http://", "").replace("/", "_").replace(".", "_")
    report_file = f"reports/directories_{safe_name}_{timestamp}.txt"

    for path in paths:
        url = f"{base_url}/{path}"
        try:
            res = requests.get(url, timeout=4)
            if res.status_code in [200, 301, 302]:
                print(color_text(f"[FOUND] {url} (Status: {res.status_code})", "green"))
                found.append(url)
            time.sleep(0.2)  # Prevent rate limiting
        except requests.exceptions.RequestException:
            pass

    if found:
        with open(report_file, "w") as f:
            for item in found:
                f.write(item + "\n")
        print(color_text(f"\n[+] Results saved to file: {report_file}", "cyan"))
    else:
        print(color_text("\n[-] No directories found.", "yellow"))
