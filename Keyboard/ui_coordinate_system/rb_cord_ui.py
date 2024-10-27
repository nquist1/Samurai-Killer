import tkinter as tk
from tkinter import messagebox
from coordinate_link import print_coordinate

def read_coordinates_from_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.readlines()
        # Convert lines to tuples of integers
        coordinates = [tuple(map(int, line.strip().split(', '))) for line in contents]
        return coordinates
    except FileNotFoundError:
        return [(0, 0) for _ in range(5)]  # Default values if file not found
    except ValueError:
        return [(0, 0) for _ in range(5)]  # Default values if there's an error in format

def on_save(popup):
    # Collect the user input
    coordinates = []
    for i in range(5):
        x_value = popup.grid_slaves(row=i, column=1)[0].get()
        y_value = popup.grid_slaves(row=i, column=2)[0].get()
        coordinates.append((x_value, y_value))

    # Save the coordinates to a file
    with open('rb_coordinates.txt', 'w') as file:
        for coord in coordinates:
            file.write(f"{coord[0]}, {coord[1]}\n")

    messagebox.showinfo("Saved", "Coordinates have been saved to 'rb_coordinates.txt'.")

def coord_form(root):
    # Create the main window
    popup = tk.Tk()
    popup.title("Coordinate Input Example")
    popup.geometry("275x400")

    count = 5
    coordinates = read_coordinates_from_file('rb_coordinates.txt')

    for i in range(count):
        # Create labels and entry fields for x and y coordinates
        x_label = tk.Label(popup, text=f"Enter coordinate {i + 1}:")
        x_label.grid(row=i, column=0, padx=5, pady=5)

        x_entry = tk.Entry(popup, width=5)
        x_entry.grid(row=i, column=1, padx=5, pady=5)
        x_entry.insert(0, coordinates[i][0])  # Pre-fill with x coordinate

        y_label = tk.Label(popup, text=" ")
        y_label.grid(row=i, column=2, padx=5, pady=5)

        y_entry = tk.Entry(popup, width=5)
        y_entry.grid(row=i, column=2, padx=5, pady=5)
        y_entry.insert(0, coordinates[i][1])  # Pre-fill with y coordinate

    # Create a submit button
    submit_button = tk.Button(
        popup, text="Save", command=lambda: on_save(popup)
    )
    submit_button.grid(row=count, columnspan=4, pady=10)

    quit_button = tk.Button(
        popup, text="Quit", command=lambda: go_back_form(root, popup)
    )
    quit_button.grid(row=count + 1, columnspan=4, pady=10)

    popup.mainloop()

def go_back_form(main_window, current):
    current.destroy()
    main_window.deiconify()

# Example usage
if __name__ == "__main__":
    main_window = tk.Tk()
    main_window.title("Main Window")
    main_window.geometry("300x200")
    open_button = tk.Button(main_window, text="Open Coordinate Form", command=lambda: coord_form(main_window))
    open_button.pack(pady=20)
    main_window.mainloop()
