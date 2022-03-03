import pyautogui
import webbrowser
import time


message = input("What message do you want to spam")
repeats = int(input("How many times do you want to spam this shit"))
delay = int(input("How many ms do you want to wait inbetween"))

isLoaded = input("Press enter when your discord is loaded")



print("You have five seconds before the spam starts")

time.sleep(5)


for i in range (0,repeats):
    if message != "":
        pyautogui.typewrite(message)
        pyautogui.press("enter")
    else:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")
        
        
        time.sleep(delay/1000)
        
        print("Done\n")