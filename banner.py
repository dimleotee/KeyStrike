from pyfiglet import Figlet
from utils.colors import color_text

def show_banner():
    fig = Figlet(font='slant')
    print(color_text(fig.renderText('KeyStrike'), 'cyan'))
    print(color_text("KeyStrike - Ethical Brute-Force Toolkit", "green"))
    print(color_text("For Educational Use Only!\n", "green"))

