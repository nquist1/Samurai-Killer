"""File processing for coordinates"""


def read_file(filename):
    """Read in file and save contents to an array"""
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            contents = file.readlines()

        # Convert the lines to a list of tuples (x, y)
        coords = []
        for line in contents:
            x, y = line.strip().split(", ")
            coords.append((int(x), int(y)))

        return coords

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except ValueError:
        print(
            "Error: Invalid line format. Each line should contain two integers separated by a comma."
        )
        return None


def print_coordinate(coords, line_number):
    """Print coordinates for debugging"""
    if 0 <= line_number < len(coords):
        x, y = coords[line_number]
        print(f"{x} {y}")
    else:
        print("Error: Line number out of range.")


if __name__ == "__main__":
    # Specify the filename
    NAME_OF_FILE = "rb_coordinates.txt"

    # Read coordinates from the file
    coordinates = read_file(NAME_OF_FILE)

    for i in range(5):
        print_coordinate(coordinates, i)

