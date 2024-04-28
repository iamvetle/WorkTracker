import time, winsound, sys, os, platform
from colorama import Fore, init

init()

score = 0

worktime = 25
shortbreaktime = 5
longbreaktime = 15

os_system = platform.system()
clear_command = ""

if os_system == "Windows":
    clear_command = "cls"
else:
    clear_command = "clear"


# CLASSES
class turnColor:
        @staticmethod # Edits color of text
        def change(text, choice):
            color_list = ["RED", "BLACK", "BLUE", "CYAN", "GREEN", "MAGNETA", "WHITE", "YELLOW"]
            choice = choice.upper()
            if choice in color_list:
                color_text = getattr(Fore, choice) + text + Fore.RESET
                return color_text
        
        @staticmethod # Prints text with color
        def send(text, choice):
            color_list = ["RED", "BLACK", "BLUE", "CYAN", "GREEN", "MAGNETA", "WHITE", "YELLOW"]
            choice = choice.upper()
            if choice in color_list:
                color_text = getattr(Fore, choice) + text + Fore.RESET
                print(color_text)

try:   
    def timer(countdown):
        # worktime, shortbreaktime or longbreaktime
        global score
        winsound.Beep(2450, 100)
        
        mode = ""
        end_message = ""
        
        if countdown == worktime:
            mode = "WORK"
            end_message = "Work session finished!"
            color_choice = "RED"
        else:            
            mode = "BREAK"
            end_message = "Break over!"
            color_choice = "GREEN"

        print(turnColor.change(f"{mode}: ", color_choice), end="")
        print(f"{countdown} min left ", end="")
        print(turnColor.change(f"\t(SCORE: {score})", "YELLOW"))
        time.sleep(0.5)
        while True:
            time.sleep(60)
            countdown -= 1
            
            os.system(clear_command)
            
            print(turnColor.change(f"{mode}: ", color_choice), end="")
            print(f"{countdown} min left ", end="")
            print(turnColor.change(f"\t(SCORE: {score})", "YELLOW"))

            if countdown == 0:
                time.sleep(1)
                for times in range(0,4):
                  winsound.Beep(2450, 100)
                if mode == "WORK":
                   score += 1
                os.system(clear_command)
                print(turnColor.change(f"{mode} ", color_choice), end="")
                print(f"{countdown} min left ", end="")
                print(turnColor.change(f"\t(SCORE: {score})", "YELLOW"))
                
                print("\n", end_message, sep="")
                return

    # Beginning
    os.system(clear_command)
    input(turnColor.change(f"Press ENTER to start '{turnColor.change('The Work Tracker', 'RED')}' ", "CYAN"))
    time.sleep(0.5)
    os.system(clear_command)
    while True:
        for times in range(1,3):
            timer(worktime)
            time.sleep(1)            
            input(turnColor.change(f"\n{worktime} min work finished. Press ENTER to start a short {shortbreaktime} min break.", "BLUE"))
            
            time.sleep(1)
            os.system(clear_command)
            timer(shortbreaktime)
            input(turnColor.change(f"\n{shortbreaktime} min break finished. Press ENTER to start a {worktime} min work session.", "BLUE"))
            
            time.sleep(1)
            os.system(clear_command)
        timer(worktime)
        input(turnColor.change(f"\n{worktime} min work finished. Press ENTER to start a long {longbreaktime} min break.", "BLUE"))
        time.sleep(1)
        os.system(clear_command)
        
        timer(longbreaktime)
        time.sleep(1)
        os.system(clear_command)
        input(turnColor.change(f"\n{longbreaktime} min long break finished. Press ENTER to start a {worktime} min work session.", "BLUE"))
        time.sleep(1)
        os.system(clear_command)        
except KeyboardInterrupt:
    time.sleep(0.5)
    os.system(clear_command)
    print(turnColor.change(f"(SCORE: {score}) ", "YELLOW"), end="")
    print(turnColor.change(f"\tYou worked for {score * worktime} min", "BLUE"))
    time.sleep(0.25)
    sys.exit()