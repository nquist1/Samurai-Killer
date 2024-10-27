def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.readlines()

        # Convert the lines to a list of tuples (x, y)
        coordinates = []
        for line in contents:
            x, y = line.strip().split(', ')
            coordinates.append((int(x), int(y)))

        return coordinates

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except ValueError:
        print("Error: Invalid line format. Each line should contain two integers separated by a comma.")
        return None

def print_coordinate(coordinates, line_number):
    if 0 <= line_number < len(coordinates):
        x, y = coordinates[line_number]
        print(f"{x} {y}")
    else:
        print("Error: Line number out of range.")

if __name__ == "__main__":
    # Specify the filename
    filename = 'rb_coordinates.txt'
    
    # Read coordinates from the file
    coordinates = read_file(filename)
    
    for i in range(5):
        print_coordinate(coordinates, i)