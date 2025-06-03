"""
DISCLAIMER:
This tool is intended **strictly for educational and authorized testing purposes only**.
You must obtain **explicit permission** from the owner of any system you target with this script.
Unauthorized access or misuse of this tool **may be illegal** and can result in **criminal charges**.

The developer and contributors of KeyStrike **are not responsible** for any misuse or damage caused.
Use responsibly and ethically.
"""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from utils.colors import color_text
import os
import subprocess
from datetime import datetime

def run():
    print(color_text("\n[+] Starting PDF Report Exporter...\n", "cyan"))
    reports_dir = "reports"
    files = [f for f in os.listdir(reports_dir) if f.endswith(".txt")]

    if not files:
        print(color_text("[-] No TXT reports found.", "yellow"))
        return

    print("Available TXT reports:")
    for i, file in enumerate(files, 1):
        print(color_text(f"{i}. {file}", "blue"))

    try:
        choice = int(input("\nEnter report number to convert to PDF: "))
        selected_file = files[choice - 1]
    except:
        print(color_text("[!] Invalid selection.", "red"))
        return

    txt_path = os.path.join(reports_dir, selected_file)
    pdf_name = selected_file.replace(".txt", "_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".pdf")
    pdf_path = os.path.join(reports_dir, pdf_name)

    with open(txt_path, "r") as f:
        lines = f.readlines()

    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Courier", 10)
    width, height = letter

    y = height - 40
    c.drawString(50, y, f"KeyStrike Report: {selected_file}")
    y -= 30

    for line in lines:
        if y < 40:
            c.showPage()
            c.setFont("Courier", 10)
            y = height - 40
        c.drawString(50, y, line.strip())
        y -= 15

    c.save()
    print(color_text(f"\n[+] PDF saved to: {pdf_path}", "cyan"))

    try:
        subprocess.run(["evince", pdf_path], check=False)
    except Exception:
        print(color_text("[!] Could not auto-open the PDF.", "red"))
