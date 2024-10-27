import os
import time
import keyboard
import pyautogui

from coordinate_link import read_file


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


# Confirm image is found on screen with 85% confidence
def image_choose(i):
    print(files[i])
    old_path = result
    add_to_path = files[i]
    new_path = os.path.join(old_path, add_to_path)
    print(new_path)
    location_on_screen = pyautogui.locateOnScreen(new_path, confidence=0.85)
    return located(location_on_screen)

# If image is found move to image and click
def located(location_on_screen):
    # Confirm image is found on screen
    if location_on_screen:
        pyautogui.moveTo(location_on_screen, duration=0.5)
        pyautogui.click(pyautogui.center(location_on_screen))
        print("Screenshot found and clicked!")
    else:
        print("Image not found on screen")


# Enters the coordinates into the game
def enter_cord(user_input1,user_input2):
    pyautogui.press("tab")
    for i in range(len(user_input1)):
        pyautogui.press(i)
    pyautogui.press("tab")
    for i in range(len(user_input2)):
        pyautogui.press(i)
    pyautogui.press("enter")

# Example usage
if __name__ == "__main__":

    filename = 'rb_coordinates.txt'

    coordinates = read_file(filename)
    if coordinates is not None:
    # Loop through each coordinate tuple
        print("\nCoordinates to attack")
        for x, y in coordinates:
            print(f"X: {x}, Y: {y}")
    else:
        print("No coordinates to display.")
    print("")

    