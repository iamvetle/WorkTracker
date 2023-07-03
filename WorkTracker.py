import time, winsound, sys, os, platform
import turnColor

score = 0

os_system = platform.system()
clear_command = ""

if os_system == "Windows":
    clear_command = "cls"
else:
    clear_command = "clear"

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

        print(turnColor.Change(f"{mode}: ", color_choice), end="")
        print(f"{countdown} min left ", end="")
        print(turnColor.Change(f"\t(SCORE: {score})", "YELLOW"))
        time.sleep(0.5)
        while True:
            time.sleep(60)
            countdown -= 1
            
            os.system(clear_command)
            
            print(turnColor.Change(f"{mode}: ", color_choice), end="")
            print(f"{countdown} min left ", end="")
            print(turnColor.Change(f"\t(SCORE: {score})", "YELLOW"))

            if countdown == 0:
                time.sleep(1)
                for times in range(0,4):
                  winsound.Beep(2450, 100)
                if mode == "WORK":
                   score += 1
                os.system(clear_command)
                print(turnColor.Change(f"{mode} ", color_choice), end="")
                print(f"{countdown} min left ", end="")
                print(turnColor.Change(f"\t(SCORE: {score})", "YELLOW"))
                
                print("\n", end_message, sep="")
                return

    # Beginning
    os.system(clear_command)
    input(turnColor.Change(f"Press ENTER to start '{turnColor.Change('The Work Tracker', 'RED')}' ", "CYAN"))
    time.sleep(0.5)
    os.system(clear_command)
    while True:
        for times in range(1,3):
            timer(25)
            time.sleep(1)            
            input(turnColor.Change("\n25 min work finished. Press ENTER to start a short 5 min break.", "BLUE"))
            
            time.sleep(1)
            os.system(clear_command)
            timer(5)
            input(turnColor.Change("\n5 min break finished. Press ENTER to start a 25 min work session.", "BLUE"))
            
            time.sleep(1)
            os.system(clear_command)
        timer(25)
        input(turnColor.Change("\n25 min work finished. Press ENTER to start a long 15 min break.", "BLUE"))
        time.sleep(1)
        os.system(clear_command)
        
        timer(15)
        time.sleep(1)
        os.system(clear_command)
        input(turnColor.Change("\n15 min long break finished. Press ENTER to start a 25 min work session.", "BLUE"))
        time.sleep(1)
        os.system(clear_command)        
except KeyboardInterrupt:
    time.sleep(0.5)
    os.system(clear_command)
    print(turnColor.Change(f"(SCORE: {score}) ", "YELLOW"), end="")
    print(turnColor.Change(f"\tYou worked for {score * 25} min", "BLUE"))
    time.sleep(0.25)
    sys.exit()