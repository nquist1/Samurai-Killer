import tkinter as tk
from tkinter import messagebox


def on_submit(x, y):
    try:
        x = float(x.get())
        y = float(y.get())
        messagebox.showinfo("Coordinates", f"You entered: (x: {x}, y: {y})")
    except ValueError:
        messagebox.showerror(
            "Input Error", "Please enter valid numeric values for x and y."
        )


def coord_form(root):
    # Create the main window
    popup = tk.Tk()
    popup.title("Coordinate Input Example")
    popup.geometry("350x200")

    # Create labels and entry fields for x and y coordinates
    x_label = tk.Label(popup, text="Enter coordinates:")
    x_label.grid(row=0, column=0, padx=5, pady=5)

    x_entry = tk.Entry(popup, width=5)
    x_entry.grid(row=0, column=1, padx=5, pady=5)

    y_label = tk.Label(popup, text=" ")
    y_label.grid(row=0, column=2, padx=5, pady=5)

    y_entry = tk.Entry(popup, width=5)
    y_entry.grid(row=0, column=2, padx=5, pady=5)

    # Create a submit button
    submit_button = tk.Button(
        popup, text="Submit", command=lambda x=x_entry, y=y_entry: on_submit(x, y)
    )
    submit_button.grid(row=1, columnspan=4, pady=10)

    quit_button = tk.Button(
        popup, text="Quit", command=lambda x=root, y=popup: go_back_form(x, y)
    )
    quit_button.grid(row=2, columnspan=4, pady=10)

    popup.mainloop()


def go_back_form(main_window, current):
    current.destroy()
    main_window.deiconify()
