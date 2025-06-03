# KeyStrike
![GitHub repo stars](https://img.shields.io/github/stars/dimleotee/KeyStrike?style=social)
**KeyStrike** is an ethical brute-force and reconnaissance toolkit built in Python for educational and awareness purposes. It helps security professionals and learners understand how attackers locate and attempt to access admin panels, directories, subdomains, and vulnerable services using brute force or scanning techniques.

> **Created by:** Teejay
> 
> **Status:** Active & Maintained

---

## Features

* ✅ **FTP Brute Forcer**
* -  Multithreaded FTP Brute Force with Clean Output and Logging
* ✅ **SSH Brute Forcer**
* ✅ **Admin Panel Finder (HTTP + HTTPS)**
* ✅ **Subdomain Scanner**
* ✅ **Directory Brute Forcer**
* ✅ **Report Generator (PDF / HTML)**

---

## Installation

```bash
# Clone the repository
https://github.com/dimleotee/KeyStrike.git

# Navigate into the project folder
cd KeyStrike

# Create and activate virtual environment
python3 -m venv keystike-env
source keystike-env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
python3 main.py
```

Follow the menu to choose between:

* FTP/SSH brute force
* Admin panel search
* Subdomain enumeration
* Directory brute forcing
* Report exporting (PDF/HTML)
* The FTP Brute Forcer now supports multithreading, logs successful credentials to success_log.txt, and hides failed attempts for cleaner output.

---

## Project Structure

```
KeyStrike/
├── banner.py                 # ASCII intro banner
├── main.py                   # Main interactive menu
├── wordlist.txt              # <- Must be added manually
├── requirements.txt          # Python dependencies
├── tools/                    # Core modules (ftp_brute, admin_finder, etc.)
├── utils/                    # Utility functions like color output
├── reports/                  # Exported PDF/HTML reports
├── keystike-env/             # (Optional) Python venv directory
```

> **Note:** `wordlist.txt` is **excluded** from the repository. Please provide your own wordlist (e.g., extracted from rockyou.txt or other sources).

---

## Recommendations

* Use only in a **safe lab environment** or against systems you own or have permission to test.
* Pair it with tools like Wireshark, Burp Suite, or Gophish for a full red-team simulation.
* Use `rockyou.txt` or filtered custom wordlists for better brute force accuracy.

---

## License

KeyStrike is licensed for **educational use only**. Unauthorized or malicious use against live targets is **strictly prohibited**.

---

## Contributors

* **Teejay** - Project Lead & Developer
* **Professor Ace** - Architect & Mentor

## Description
---
 **What's Next?**
We’re excited to announce that KeyStrike v2 will introduce **LLM (Large Language Model) integration** to elevate offensive security automation. The upcoming version will feature an AI controller to:

- Recommend brute-force strategies based on target response.
- Dynamically select the most effective scanning modules.
- Log and summarize attacks in natural language for reports.
- Assist red teamers in real-time decisions.

🔒 KeyStrike v1 is just the beginning — the next evolution brings AI to ethical hacking.


## Contact

For collaboration, reach out via GitHub
