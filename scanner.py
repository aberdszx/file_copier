import shutil
import time
from datetime import datetime
import os
import PySimpleGUI as sg
import pyautogui


# Function to copy from desktop to NAS
def copy(source, destination):
    print("Copying " + source)
    shutil.copytree(source, destination,dirs_exist_ok=True)


# Delete the copied directories
def delete(source):
    shutil.rmtree(source, ignore_errors=True)
    print("deleted")


def mkdir():
    dir_list = ["IT", "HR", "MOD", "FOD", "OBC-OPE", "MARKETING", "ADMIN", "ACCOUNTING", "EXEC", "MAINTENANCE", "BDD"]
    for item in dir_list:
        path = os.path.join(r"C:\Users\adrian-pc\Desktop", item)
        os.mkdir(path)
    print("Directories created")



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


sources = [r"C:\Users\MQ-SCAN\Desktop", r"C:\Users\MQ-SCAN\Downloads", r"C:\Users\MQ-SCAN\Documents"]
destination = r"\\mrq-server\it\SCANNED_FILES"
while time_detection():
    for source in sources:
        copy(source, destination)
        delete(source)
    mkdir()
    pyautogui.hotkey("win", "d")
    time.sleep(1)
    window_creation()
    time.sleep(15)
    os.system("shutdown /r /t 10")
    if window_creation() == "OK":
        print(window_creation())
        os.system("shutdown /r /t 10")
        break
    elif window_creation() == "Extend":
        print(window_creation())
        os.system("shutdown /r /t 900")
        break
    time.sleep()