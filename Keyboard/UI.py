"""This file is responsible for the UI and is the main program"""

import os
import tkinter as tk

from coord_ui import coord_form


def run_program(main_window, imgs_dir, img_folder):
    """Opens the UI delegated interface to edit the coords"""
    main_window.withdraw()
    path_to_folder = os.path.join(*imgs_dir, img_folder)
    images = os.listdir(os.path.join(path_to_folder, ""))
    print(images)
    coord_form(main_window, img_folder + ".txt")


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
