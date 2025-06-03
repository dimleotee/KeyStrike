"""
DISCLAIMER:
This tool is intended **strictly for educational and authorized testing purposes only**.
You must obtain **explicit permission** from the owner of any system you target with this script.
Unauthorized access or misuse of this tool **may be illegal** and can result in **criminal charges**.

The developer and contributors of KeyStrike **are not responsible** for any misuse or damage caused.
Use responsibly and ethically.
"""
import requests
from utils.colors import color_text
from datetime import datetime
import os

def run():
    print(color_text("\n[+] Starting Subdomain Scanner...\n", "cyan"))
    domain = input("Enter base domain (e.g., example.com): ").strip()

    # Sanitize input
    domain = domain.replace("http://", "").replace("https://", "").strip("/")
    if domain.count(".") > 2:
        print(color_text("[!] Please enter a base domain (e.g., tryhackme.com)", "red"))
        return

    subdomains = [
        "admin", "mail", "blog", "test", "dev", "cpanel", "ftp", "webmail", "vpn", "ns1", "ns2"
    ]

    found = []
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_name = domain.replace(".", "_")
    report_file = f"reports/subdomains_{safe_name}_{timestamp}.txt"

    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            res = requests.get(url, timeout=4)
            if res.status_code in [200, 301, 302]:
                print(color_text(f"[FOUND] {url}", "green"))
                found.append(url)
        except requests.exceptions.RequestException:
            pass

    if found:
        with open(report_file, "w") as f:
            for item in found:
                f.write(item + "\n")
        print(color_text(f"\n[+] Results saved to file: {report_file}", "cyan"))
    else:
        print(color_text("\n[-] No subdomains found.", "yellow"))

