from colorama import Fore, Style, init
init(autoreset=True)

def color_text(text, color):
    colors = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "cyan": Fore.CYAN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
    }
    return colors.get(color, "") + text + Style.RESET_ALL
