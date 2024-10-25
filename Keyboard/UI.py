"""This file is responsible for the UI and is the main program"""

import os
import tkinter as tk

from ui_coordinate_system.rb_cord_ui import coord_form


# Create a function to print Hello
def berimond_gg():
    """This function does xyz"""
    print("Hello")

    # berimond main code


def run_program(main_window, imgs_dir, img_folder):
    """deals with ui forms"""
    main_window.withdraw()
    img_folder = os.path.join(*imgs_dir, img_folder)
    images = os.listdir(os.path.join(img_folder, ""))
    print(images)
    coord_form(main_window)


# Add buttons

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Samurai Killer")

    DIR = ["Screenshots"]

    button_contents = [
        ["Berimond - Classic", "BerimondClassic"],
        ["Nomads", "Nomad"],
        ["RobberBarron", "RobberBarron"],
    ]

    for button in button_contents:
        new_button = tk.Button(
            root,
            text=button[0],
            command=lambda folder=button[1]: run_program(root, DIR, folder),
        )
        new_button.pack(pady=10)

    # Add a Quit button to close the window
    quit_button = tk.Button(root, text="Quit", command=root.destroy)
    quit_button.pack(pady=10)

    # Run the application
    root.mainloop()
