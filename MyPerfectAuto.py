import pyautogui as p
from time import sleep
import keyboard
import datetime
import os

tcolor = (0, 94, 194)  # Target color remains the same

def capture_and_store_coordinates():
    """
    Captures the coordinates for different points from the user and saves them to a uniquely named text file.
    The user presses the space bar to save each coordinate.
    """
    coordinates = {}
    
    for point in ['p1', 'p2', 'p3', 'p4']:
        print(f"Move the mouse to the {point} position and press the space bar.")
        while True:
            if keyboard.is_pressed('space'):
                position = p.position()  # Capture current mouse position
                print(f"Captured {point} coordinates: {position}")
                coordinates[point] = position
                sleep(1)  # Avoid multiple captures due to key press delay
                break

    # Create a unique filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'coordinates_{timestamp}.txt'
    
    try:
        # Write coordinates to the unique file
        with open(filename, 'w') as f:
            for key, value in coordinates.items():
                f.write(f"{key}:{value[0]},{value[1]}\n")
        print(f"Coordinates saved to '{filename}'.")
    except IOError as e:
        print(f"Error writing to file: {e}")

def load_coordinates_from_file():
    """
    Reads coordinates from a file and returns them as a dictionary.
    """
    coordinates = {}
    filename = 'coordinates.txt'
    
    if not os.path.exists(filename):
        print(f"Error: '{filename}' file not found. Please capture coordinates first.")
        exit(1)
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                key, value = line.strip().split(':')
                x, y = map(int, value.split(','))
                coordinates[key] = (x, y)
    except IOError as e:
        print(f"Error reading from file: {e}")
        exit(1)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        exit(1)
    
    return coordinates

def check_and_click(position, target_color):
    """
    Moves the mouse to the given position and checks the pixel color.
    Clicks if the color matches the target color.
    """
    while True:
        try:
            p.moveTo(position)
            getcolor = p.pixel(position[0], position[1])
            if getcolor == target_color:
                p.click()
                break
            else:
                sleep(0.5)
        except Exception as e:
            print(f"Error while checking and clicking: {e}")
            sleep(1)

# Main program flow
print("Do you want to (1) Capture coordinates or (2) Execute the program?")
choice = input("Enter 1 or 2: ").strip()

try:
    if choice == '1':
        capture_and_store_coordinates()
    elif choice == '2':
        # Load coordinates from file
        coordinates = load_coordinates_from_file()

        # Assign loaded coordinates to p1, p2, p3, p4
        p1 = coordinates['p1']
        p2 = coordinates['p2']
        p3 = coordinates['p3']
        p4 = coordinates['p4']

        # Get the number of iterations from the user
        try:
            n = int(input("Enter the number of times to execute the tasks: ").strip())
            sleep(3)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            exit(1)

        # Main loop to execute the tasks
        for _ in range(n):
            check_and_click(p1, tcolor)
            check_and_click(p2, tcolor)
            sleep(2)
            check_and_click(p3, tcolor)
            sleep(5)
            p.hotkey('ctrl', 'r')
            sleep(2)
            p.hotkey('ctrl', 'r')# Refresh the page
            sleep(10)
            check_and_click(p4, tcolor)
    else:
        print("Invalid choice. Please enter 1 to capture or 2 to execute.")
        exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
