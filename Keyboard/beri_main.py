# Stairz
"""sdklfj"""

import os


def run_program(img_directory, event_imgs):
    """skdjf"""
    img_folder = os.path.join(*img_directory, event_imgs)
    images = os.listdir(img_folder)
    print(images)
    # if img_directory is None:
    #     return
