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


# Add a Hello button
hello_button = tk.Button(
    root,
    text="Berimond - Classic",
    command=lambda: run_program(DIR, "BerimondClassic/"),
)
hello_button.pack(pady=10)

# Add a Quit button to close the window
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

# Run the application
root.mainloop()
