#thanks for downloading this
# once you start the program it will keep on going forever until you press R

import pyautogui
import time
import keyboard

def click():
    time.sleep(0.1)
    pyautogui.click()

print("Autoclicker starting in 5 seconds...")
time.sleep(5)
print("Autoclicker running. Press 'R' to stop...")

while True:
    if keyboard.is_pressed('r'):
        print("Stopping autoclicker.")
        break
    click()
