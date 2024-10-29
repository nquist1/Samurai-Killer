"""This file runs the UIs for the different events allowing for coordinate customization"""

import tkinter as tk
from tkinter import messagebox

from coordinate_link import FILE_FOLDER

NUMBER_OF_COORDS = 5


def read_coordinates_from_file(filename):
    """Read in coords or default them to 0"""
    try:
        with open(FILE_FOLDER + filename, "r", encoding="UTF-8") as file:
            contents = file.readlines()
        # Convert lines to tuples of integers
        coordinates = [tuple(map(int, line.strip().split(", "))) for line in contents]
        return coordinates
    except FileNotFoundError:
        return [
            (0, 0) for _ in range(NUMBER_OF_COORDS)
        ]  # Default values if file not found
    except ValueError:
        return [
            (0, 0) for _ in range(NUMBER_OF_COORDS)
        ]  # Default values if there's an error in format


def on_save(popup, text_file):
    """Save the inputed values to file"""
    # Collect the user input
    coordinates = []
    for i in range(NUMBER_OF_COORDS):
        x_value = popup.grid_slaves(row=i, column=1)[0].get()
        y_value = popup.grid_slaves(row=i, column=2)[0].get()
        coordinates.append((x_value, y_value))

    # Save the coordinates to a file
    with open(FILE_FOLDER + text_file, "w", encoding="UTF-8") as file:
        for coord in coordinates:
            file.write(f"{coord[0]}, {coord[1]}\n")

    messagebox.showinfo(
        "Saved", f"Coordinates have been saved to '{FILE_FOLDER}{text_file}'."
    )


def coord_form(ui_window, file_read):
    """Create the UI for customizing the coordinates"""
    # Create the main window
    popup = tk.Tk()
    popup.title("Coordinate Input Example")
    popup.geometry("275x400")

    # TODO: make this file work for each UI not just robberbarron
    count = 5
    coordinates = read_coordinates_from_file(file_read)

    for i in range(count):
        # Create labels and entry fields for x and y coordinates
        x_label = tk.Label(popup, text=f"Enter coordinate {i + 1}:")
        x_label.grid(row=i, column=0, padx=5, pady=5)

        x_entry = tk.Entry(popup, width=5)
        x_entry.grid(row=i, column=1, padx=5, pady=5)
        x_entry.insert(0, str(coordinates[i][0]))  # Pre-fill with x coordinate

        y_label = tk.Label(popup, text=" ")
        y_label.grid(row=i, column=2, padx=5, pady=5)

        y_entry = tk.Entry(popup, width=5)
        y_entry.grid(row=i, column=2, padx=5, pady=5)
        y_entry.insert(0, str(coordinates[i][1]))  # Pre-fill with y coordinate

    # Create a submit button
    submit_button = tk.Button(
        popup, text="Save", command=lambda: on_save(popup, file_read)
    )
    submit_button.grid(row=count, columnspan=4, pady=10)

    quit_button = tk.Button(
        popup, text="Quit", command=lambda: go_back_form(ui_window, popup)
    )
    quit_button.grid(row=count + 1, columnspan=4, pady=10)

    popup.mainloop()


def go_back_form(main_window, current):
    """Destroy coordinates form and show the Main Menu"""
    # TODO: read saved text input back to file
    current.destroy()
    main_window.deiconify()


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("300x200")
    open_button = tk.Button(
        root,
        text="Open Coordinate Form",
        command=lambda: coord_form(root),
    )
    open_button.pack(pady=20)
    root.mainloop()
