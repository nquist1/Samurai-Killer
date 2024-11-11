import os
import time
import keyboard
import pyautogui
import random

# Finding Folder
def find_folder(folder_name):
    home_directory = os.path.expanduser("~")
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
        pyautogui.moveTo(location_on_screen, duration=0.2)
        pyautogui.click(pyautogui.center(location_on_screen))
        print("Screenshot found and clicked!")
        return True
    else:
        print("Image not found on screen")
        return False

def image_choose(i, max_retries=3):
    old_path = result
    add_to_path = files[i]
    new_path = os.path.join(old_path, add_to_path)
    print(f"Attempting to locate image: {new_path}")
    
    retries = 0
    while retries < max_retries:
        try:
            location_on_screen = pyautogui.locateOnScreen(new_path, confidence=0.85)
            if located(location_on_screen):
                return True  # Successfully found and clicked
            else:
                print(f"Attempt {retries + 1} failed. Retrying...")
                retries += 1
                handle_failure()  # Attempt to handle any popup or interference
                time.sleep(1)  # Brief pause before retrying

        except pyautogui.ImageNotFoundException as e:
            print(f"Image not found: {e}. Retrying...")
            handle_failure()
            retries += 1
            time.sleep(1)
    
    print(f"Failed to locate image after {max_retries} attempts.")
    return False  # Failed after max retries

# Function to handle the failure case, e.g., closing a popup
def handle_failure():
    popup_image_index = 13  # Use an index for popup image in `files`
    if popup_image_index < len(files):
        popup_path = os.path.join(result, files[popup_image_index])
        try:
            popup_location = pyautogui.locateOnScreen(popup_path, confidence=0.85)
            if popup_location:
                print("Popup detected! Closing it.")
                pyautogui.click(pyautogui.center(popup_location))
                time.sleep(1)  # Wait for the popup to close
            else:
                print("No popup detected. Retrying main task.")
        except pyautogui.ImageNotFoundException:
            print("Popup image not found. Continuing.")
    else:
        print("Popup image index is out of range. Please verify the popup image path.")

# Main loop
while True:
    if keyboard.is_pressed("q"):  # Press "q" to exit
        break
    random_number2 = random.randint(1, 2)
    go = True
    timer = 0
    commanders = 0
    while go:
        image_choose(0)
        time.sleep(random_number2)
        image_choose(1)
        time.sleep(random_number2)
        image_choose(2)
        time.sleep(random_number2)
        image_choose(3)
        time.sleep(3)
        image_choose(4)
        time.sleep(random_number2)
        image_choose(5)
        time.sleep(random_number2)
        image_choose(6)
        time.sleep(random_number2)
        image_choose(7)
        time.sleep(random_number2)
        image_choose(8)
        time.sleep(random_number2)
        
        timer += 1
        commanders += 1
        
        print("I AM HEREEEEEEEE:", commanders)
        if commanders == 4:
            print("Commanders have reached 0!")
            go = False
        
        if timer == 5:
            image_choose(9)
            time.sleep(random_number2)
            image_choose(11)
            time.sleep(random_number2)
            image_choose(12)
            time.sleep(random_number2)
            image_choose(10)
            time.sleep(random_number2)
            timer = 0

    # Reset commanders and allow loop to continue
    commanders = 0
    print("Sleeping..........")
    time.sleep(240)
    go = True
