# """Locate and click image"""
#
import os

#
# import pyautogui
#
#
# def find_image(img_directory, confidence=0.8):
#     """stuff"""
#
#     while True:
#         try:
#             location = pyautogui.locateCenterOnScreen(
#                 image_castle, confidence=confidence
#             )
#             if location is not None:
#                 return location
#             return None
#         except Exception as e:
#             print("Error:", e)
#             return None
#
#
if __name__ == "__main__":
    print(os.getcwd())
    img_directory = "Screenshots/BerimondClassic/"
    os.path.exists(img_directory)
    files = os.listdir(img_directory)
    print(files)
#
#
#
# def find_target(image_target, confidence=0.5):
#     try:
#         location = pyautogui.locateOnScreen(image_target, confidence=confidence)
#         if location is not None:
#             return location
#         else:
#             return None
#     except Exception as e:
#         print("Error:", e)
#         return None
#
#
# def distance_between_points(point1, point2):
#     x1, y1 = point1
#     x2, y2 = point2  # .x, point2.y
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
#
# # Example usage
# if __name__ == "__main__":
#     image_list = [
#         "robberbaronfarv1.png",
#         "targetv1.png",
#         "checkmark.png",
#         "fillwaves.jpg",
#         "attack.jpg",
#         "checkmarkcomplete.png",
#     ]
#
#     image_order = [0, 1, 2, 3, 4, 5]
#
#     for index in range(0, 6):
#         path = os.path.join("images", image_list[image_order[index]])
#         print(f"Path: {path}")
#         found_location = find_image(path)
#         if found_location is None:
#             break
#         print("Image found at:", found_location)
#         distance = distance_between_points(pyautogui.position(), found_location)
#         length = distance / 500
#         print("length to: ", length)
#         # pyautogui.sleep(1.5)
#         pyautogui.click(found_location, duration=length, interval=0.5)  # Select Castle
#         pyautogui.click(found_location, duration=0.1)  # Select Castle
#         # time.sleep(2)
