from colorama import Fore, init

init()

# Edits color of text
def Change(text, choice):
    color_list = ["RED", "BLACK", "BLUE", "CYAN", "GREEN", "MAGNETA", "WHITE", "YELLOW"]
    choice = choice.upper()
    if choice in color_list:
        color_text = getattr(Fore, choice) + text + Fore.RESET
        return color_text

# Prints text with color
def Send(text, choice):
    color_list = ["RED", "BLACK", "BLUE", "CYAN", "GREEN", "MAGNETA", "WHITE", "YELLOW"]
    choice = choice.upper()
    if choice in color_list:
        color_text = getattr(Fore, choice) + text + Fore.RESET
        print(color_text)