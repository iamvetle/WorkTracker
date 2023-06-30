import time, winsound, sys, os
from colorama import Fore, init

init()

score = 0

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
        # 25, 5 or 15
        global score
        winsound.Beep(2450, 100)
        
        mode = ""
        end_message = ""
        
        if countdown == 25:
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
            os.system("cls")
            
            print(turnColor.change(f"{mode}: ", color_choice), end="")
            print(f"{countdown} min left ", end="")
            print(turnColor.change(f"\t(SCORE: {score})", "YELLOW"))

            if countdown == 0:
                time.sleep(1)
                for times in range(0,4):
                  winsound.Beep(2450, 100)
                if mode == "WORK":
                   score += 1
                os.system("cls")
                print(turnColor.change(f"{mode} ", color_choice), end="")
                print(f"{countdown} min left ", end="")
                print(turnColor.change(f"\t(SCORE: {score})", "YELLOW"))
                
                print("\n", end_message, sep="")
                return

    # Beginning
    os.system("cls")
    input(turnColor.change(f"Press ENTER to start '{turnColor.change('The Work Tracker', 'RED')}' ", "CYAN"))
    time.sleep(0.5)
    os.system("cls")
    while True:
        for times in range(1,3):
            timer(25)
            time.sleep(1)            
            input(turnColor.change("\n25 min work finished. Press ENTER to start a short 5 min break.", "BLUE"))
            
            time.sleep(1)
            os.system("cls")
            timer(5)
            input(turnColor.change("\n5 min break finished. Press ENTER to start a 25 min work session.", "BLUE"))
            
            time.sleep(1)
            os.system("cls")
        timer(25)
        input(turnColor.change("\n25 min work finished. Press ENTER to start a long 15 min break.", "BLUE"))
        time.sleep(1)
        os.system("cls")
        
        timer(15)
        time.sleep(1)
        os.system("cls")
        input(turnColor.change("\n15 min long break finished. Press ENTER to start a 25 min work session.", "BLUE"))
        time.sleep(1)
        os.system("cls")        
except KeyboardInterrupt:
    time.sleep(0.5)
    os.system("cls")
    print(turnColor.change(f"(SCORE: {score}) ", "YELLOW"), end="")
    print(turnColor.change(f"\tYou worked for {score * 25} min", "BLUE"))
    input()
    time.sleep(0.25)
    sys.exit()