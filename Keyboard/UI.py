#Stairz

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Samurai Killer")

# Create a function to print Hello
def berimond_gg():
    print("Hello")

    #berimond main code

# Add a Hello button
hello_button = tk.Button(root, text="Berimond - Classic", command=berimond_gg)
hello_button.pack(pady=10)

# Add a Quit button to close the window
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

# Run the application
root.mainloop()