import tkinter as tk
from tkinter import messagebox

def on_submit():
    try:
        x = float(x_entry.get())
        y = float(y_entry.get())
        messagebox.showinfo("Coordinates", f"You entered: (x: {x}, y: {y})")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for x and y.")

# Create the main window
root = tk.Tk()
root.title("Coordinate Input Example")
root.geometry("350x100")

# Create labels and entry fields for x and y coordinates
x_label = tk.Label(root, text="Enter coordinates:")
x_label.grid(row=0, column=0, padx=5, pady=5)

x_entry = tk.Entry(root, width = 5)
x_entry.grid(row=0, column=1, padx=5, pady=5)

y_label = tk.Label(root, text=" ")
y_label.grid(row=0, column=2, padx=5, pady=5)

y_entry = tk.Entry(root,width = 5)
y_entry.grid(row=0, column=2, padx=5, pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=1, columnspan=4, pady=10)

# Start the main loop
root.mainloop()
