from banner import show_banner
from tools import pdf_converter
from tools import ftp_brute, ssh_brute, admin_finder, subdomain_finder, directory_finder, report_converter
from utils.colors import color_text
import sys

def main():
    show_banner()
    print(color_text("Created by: Teejay", "green")) 
    print()

    print(color_text("1. FTP Brute Force", "yellow"))
    print(color_text("2. SSH Brute Forcer", "yellow"))
    print(color_text("3. Admin Panel Finder", "yellow"))
    print(color_text("4. Subdomain Finder", "blue"))
    print(color_text("5. Directory Brute Forcer", "blue"))
    print(color_text("6. Report Converter (HTML)", "blue"))
    print(color_text("7. Export Report as PDF", "blue"))
    print(color_text("8. Exit", "red"))

    choice = input(color_text("\nChoose an option: ", "green"))

    if choice == "1":
        ftp_brute.run()
    elif choice == "2":
        ssh_brute.run(
)
    elif choice == "3":
        admin_finder.run() 

    elif choice == "4":
        subdomain_finder.run()

    elif choice == "5":
        directory_finder.run()

    elif choice == "6":
        report_converter.run()    

    elif choice == "7":
        pdf_converter.run()

    elif choice == "8":
        print(color_text("Goodbye!", "blue"))
    else:
        print(color_text("Invalid choice.", "red"))

if __name__ == "__main__":
    main()

