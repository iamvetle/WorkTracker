from colorama import Fore, init

init()

# Edits color of text
def Turn(text, **kwargs):
    color_list = ["red", "black", "blue", "cyan", "green", "magneta", "white", "yellow"]
    if "color" in kwargs:
        if kwargs["color"] in color_list:
            choice = kwargs["color"].upper()
            color_text = getattr(Fore, choice) + text + Fore.RESET
            return color_text
        else:
            return "Error: That color doesn't exist.."

# Prints text with color
def Send(text, **kwargs):
    color_list = ["red", "black", "blue", "cyan", "green", "magneta", "white", "yellow"]
    if "color" in kwargs:
        if kwargs["color"] in color_list:
            choice = kwargs["color"].upper()
            color_text = getattr(Fore, choice) + text + Fore.RESET
            print(color_text)
        else:
            print("Error: That color doesn't exist..")   

if __name__ == "__main__":            
    Send("Example", color="red")
    Send("Example", color="bruwn")
    test = Turn("Example", color="green")
    test2 = Turn("Example", color="yullow")
    print(test)
    print(test2)