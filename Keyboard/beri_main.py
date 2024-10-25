# Stairz
"""sdklfj"""

import os

from ui_coordinate_system.rb_cord_ui import coord_form


def run_beri(main_window, img_directory, event_imgs):
    """skdjf"""
    img_folder = os.path.join(*img_directory, event_imgs)
    images = os.listdir(os.path.join(img_folder, ""))
    print(images)
    coord_form(main_window)
    # if img_directory is None:
    #     return
