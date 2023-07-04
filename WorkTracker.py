import time, winsound, sys, os, platform
from turnColor import Turn

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

score = 0

os_system = platform.system()
clear_command = ""

if os_system == "Windows":
    clear_command = "cls"
else:
    clear_command = "clear"

try:
    hide_cursor()   
    def timer(countdown):
        # 25, 5 or 15
        global score
        winsound.Beep(2450, 100)
        
        mode = ""
        end_message = ""
        
        if countdown == 25:
            mode = "WORK"
            end_message = "Work session finished!"
            color_choice = "red"
        else:            
            mode = "BREAK"
            end_message = "Break over!"
            color_choice = "green"

        print(Turn(f"{mode}: ", color=color_choice), end="")
        print(f"{countdown} min left ", end="")
        print(Turn(f"\t(SCORE: {score})", color="yellow"))
        time.sleep(0.5)
        while True:
            time.sleep(60)
            countdown -= 1
            
            os.system(clear_command)
            
            print(Turn(f"{mode}: ", color=color_choice), end="")
            print(f"{countdown} min left ", end="")
            print(Turn(f"\t(SCORE: {score})", color="yellow"))

            if countdown == 0:
                time.sleep(1)
                for times in range(1,4):
                  winsound.Beep(2450, 100)
                  time.sleep(0.50)
                if mode == "WORK":
                   score += 1
                os.system(clear_command)
                print(Turn(f"{mode} ", color=color_choice), end="")
                print(f"{countdown} min left ", end="")
                print(Turn(f"\t(SCORE: {score})", color="yellow"))
                
                print("\n", end_message, sep="")
                return

    # Beginning
    os.system(clear_command)
    input(Turn(f"Press ENTER to start '{Turn('The Work Tracker', color='red')}' ", color="cyan")) 
    time.sleep(0.5)
    os.system(clear_command)
    while True:
        for times in range(1,3):
            timer(25)
            time.sleep(1)            
            input(Turn("\n25 min work finished. Press ENTER to start a short 5 min break.", color="blue")) 
            
            time.sleep(1)
            os.system(clear_command)
            timer(5)
            input(Turn("\n5 min break finished. Press ENTER to start a 25 min work session.", color="blue")) 
            
            time.sleep(1)
            os.system(clear_command)
        timer(25)
        input(Turn("\n25 min work finished. Press ENTER to start a long 15 min break.", color="blue")) 
        time.sleep(1)
        os.system(clear_command)
        
        timer(15)
        time.sleep(1)
        os.system(clear_command)
        input(Turn("\n15 min long break finished. Press ENTER to start a 25 min work session.", color="blue")) 
        time.sleep(1)
        os.system(clear_command)        
except KeyboardInterrupt:
    time.sleep(0.5)
    os.system(clear_command)
    print(Turn(f"(SCORE: {score}) ", color="yellow"), end="")
    print(Turn(f"\tYou worked for {score * 25} min", color="blue"))
    show_cursor()
    time.sleep(0.25)
    sys.exit()