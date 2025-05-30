import os
from utils.colors import color_text
from datetime import datetime

def run():
    print(color_text("\n[+] Starting Report Converter (TXT ➜ HTML)...\n", "cyan"))

    reports_dir = "reports"
    files = [f for f in os.listdir(reports_dir) if f.endswith(".txt")]

    if not files:
        print(color_text("[-] No TXT reports found to convert.", "yellow"))
        return

    print("Available reports:")
    for i, file in enumerate(files, 1):
        print(color_text(f"{i}. {file}", "blue"))

    try:
        choice = int(input("\nEnter the report number to convert: "))
        if choice < 1 or choice > len(files):
            raise ValueError
        selected_file = files[choice - 1]
    except ValueError:
        print(color_text("[!] Invalid selection. Aborting.", "red"))
        return

    txt_path = os.path.join(reports_dir, selected_file)
    with open(txt_path, "r") as f:
        lines = f.readlines()

    html_content = f"""
    <html>
    <head>
        <title>KeyStrike Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #f7f7f7; padding: 20px; }}
            h2 {{ color: #2c3e50; }}
            ul {{ background: #fff; padding: 15px; border-radius: 8px; box-shadow: 0 0 5px rgba(0,0,0,0.1); }}
            li {{ margin: 8px 0; color: #34495e; }}
        </style>
    </head>
    <body>
        <h2>KeyStrike Report: {selected_file}</h2>
        <ul>
"""
    for line in lines:
        html_content += f"            <li>{line.strip()}</li>\n"

    html_content += """
        </ul>
    </body>
    </html>
"""

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    html_filename = selected_file.replace(".txt", f"_{timestamp}.html")
    html_path = os.path.join(reports_dir, html_filename)

    with open(html_path, "w") as f:
        f.write(html_content)

    print(color_text(f"\n[+] HTML report saved as: {html_path}", "cyan"))
