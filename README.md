# MyPerfectAuto

MyPerfectAuto is a Python script designed to automate mouse actions based on specific screen coordinates and color detection. The script can either capture and store coordinates or execute automated tasks using predefined coordinates.

## Features

- **Capture Coordinates:** Move the mouse to specific positions and save their coordinates by pressing the space bar.
- **Automated Tasks:** Use the saved coordinates to automate mouse clicks and interactions.

## Installation

To use the script, you'll need Python 3 and the required libraries:

1. Clone this repository:

    ```bash
    git clone https://github.com/ohnogaurav/MyPerfectAuto.git
    cd MyPerfectAuto
    ```

2. Install the required libraries:

    ```bash
    pip install pyautogui keyboard
    ```

## Usage

### Capture Coordinates

1. Run the script to capture coordinates:

    ```bash
    python MyPerfectAuto.py capture
    ```

2. Follow the instructions to move the mouse to the desired positions and press the space bar to capture each coordinate.

3. The coordinates will be saved to a uniquely named text file in the format `coordinates_YYYYMMDD_HHMMSS.txt`.

### Execute Automated Tasks

1. Make sure you have a `coordinates.txt` file with the required coordinates. If not, capture them as described above.

2. Run the script to execute automated tasks:

    ```bash
    python MyPerfectAuto.py execute
    ```

3. Enter the number of times you want to execute the tasks.

## Handling Errors

The script includes error handling for:

- Missing or unreadable `coordinates.txt` file.
- Invalid user input.
- Issues with file operations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Gaurav

## Script Overview

The `MyPerfectAuto.py` script provides functionality to either capture screen coordinates or perform automated mouse clicks based on saved coordinates.

### Script Workflow

- **Capture Coordinates:**
  - Prompts the user to move the mouse and press the space bar to save coordinates.
  - Saves coordinates to a uniquely named text file.

- **Execute Automated Tasks:**
  - Reads coordinates from `coordinates.txt`.
  - Executes a series of automated mouse clicks based on these coordinates.
  - Handles errors and provides user feedback.

## Additional Information

- Make sure to run the script in an environment where `pyautogui` and `keyboard` can interact with the screen and keyboard.
- The script is designed to work in a standard desktop environment and might require adjustments for different setups or applications.

