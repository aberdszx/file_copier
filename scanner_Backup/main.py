import shutil
import time
from datetime import datetime
import os
import PySimpleGUI as sg
import pyautogui


# Function to copy from desktop to NAS
def copy():
    source = r"C:\Users\MQ-SCAN\Desktop"
    print("Copying " + source)
    destination = r"\\mrq-server\it\SCANNED_FILES"
    shutil.copytree(source, destination,dirs_exist_ok=True)


# Delete the copied directories
def delete():
    source_dir = r"C:\Users\MQ-SCAN\Desktop"
    dir_list = ["IT", "HR", "MOD", "FOD", "OBC-OPE", "MARKETING", "ADMIN", "ACCOUNTING", "EXEC", "MAINTENANCE", "BDD"]
    shutil.rmtree(source_dir, ignore_errors=True)
    print("deleted")
    for item in dir_list:
        path = os.path.join(source_dir, item)
        os.mkdir(path)
    print("Directories created")
    time.sleep(10)



# ADD A TKINTER WINDOW THAT DISPLAYS A MESSAGE "THIS COMPUTER WILL TURN OFF AT 5PM! CLICK EXTEND TO EXTEND FOR 15 MINUTES" AND HAVE AN EXTEND
# BUTTON TO DELAY POWER OFF WITH 15 MINUTES
def window_creation():
    layout = [[sg.Text("This computer will shutdown shortly!", font=("Arial", 45 ))],
              [sg.Button("OK", font=("Arial", 25)), sg.Button("Extend", font=("Arial", 25))]]
    window = sg.Window("Scanner Auto Backup", layout, size=(1000, 200), element_justification="center", no_titlebar=True, grab_anywhere=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "OK"):
            window.close()
            break

        elif event == "Extend":
            window.close()
            break

    return event



def time_detection():
    target_time = "17:00"
    while True:
        if datetime.now().strftime("%H:%M") == target_time:
            return True
        elif datetime.now().strftime("%H:%M") != target_time:
            print("Not Time Detected")
            time.sleep(30)



while time_detection():
    copy()
    delete()
    pyautogui.hotkey("win", "d")
    time.sleep(1)
    window_creation()
    if window_creation() == "OK":
        print(window_creation())
        os.system("shutdown /r /t 10")
        break
    elif window_creation() == "Extend":
        print(window_creation())
        os.system("shutdown /r /t 900")
        break