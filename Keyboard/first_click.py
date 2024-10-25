import os
import pyautogui
import keyboard
import time

#Finding Folder
def find_folder(folder_name):
    home_directory = os.path.expanduser('~')
    for dirpath, dirnames, filenames in os.walk(home_directory):
        if folder_name in dirnames:
            return os.path.join(dirpath, folder_name)
    return None

# Return Folder
folder_name = "BerimondClassic"
result = find_folder(folder_name)
if result:
    files = os.listdir(result)



def located(location_on_screen):
    if location_on_screen:
        pyautogui.moveTo(location_on_screen, duration=0.5)
        pyautogui.click(pyautogui.center(location_on_screen))
        print("Screenshot found and clicked!")
    else:
        print("Image not found on screen")

def image_choose(i):
    print(files[i])
    old_path = result
    add_to_path = files[i]
    new_path = os.path.join(old_path,add_to_path)
    print(new_path)
    location_on_screen = pyautogui.locateOnScreen(new_path,confidence=0.85)
    return located(location_on_screen)

image_choose(0)
pyautogui.press('tab')
pyautogui.press('4')
pyautogui.press('1')
pyautogui.press('6')
pyautogui.press('tab')
pyautogui.press('1')
pyautogui.press('1')
pyautogui.press('5')
pyautogui.press('9')
pyautogui.press('enter')
time.sleep(2)
image_choose(1)
time.sleep(1.5)
image_choose(2)
time.sleep(2)
image_choose(3)
time.sleep(.5)
image_choose(4)
time.sleep(1.5)
image_choose(5)
time.sleep(.7)
image_choose(6)