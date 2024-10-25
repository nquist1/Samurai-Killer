"""This file is responsible for the UI and is the main program"""

import tkinter as tk

from beri_main import run_program

# Create the main window
root = tk.Tk()
root.title("Samurai Killer")

DIR = ["Screenshots"]


# Create a function to print Hello
def berimond_gg():
    """This function does xyz"""
    print("Hello")

    # berimond main code


button_contents = [["Berimond - Classic", "BerimondClassic"], ["Nomads", "Nomad"]]

# Add buttons
for button in button_contents:
    new_button = tk.Button(
        root,
        text=button[0],
        command=lambda folder=button[1]: run_program(DIR, folder),
    )
    new_button.pack(pady=10)

# Add a Quit button to close the window
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

# Run the application
root.mainloop()
