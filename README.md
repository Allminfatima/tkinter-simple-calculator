# Tkinter Simple Calculator

A simple calculator application built with Python's Tkinter library. This project showcases basic arithmetic operations including addition, subtraction, multiplication, and division. The application features a clean and user-friendly graphical interface with custom styling. It provides a straightforward way to perform calculations with error handling and a clear function. Perfect for learning how to build GUI applications with Tkinter.

## Features

- **Basic Operations**: Supports addition, subtraction, multiplication, and division.
- **Custom Font**: Uses a custom font for a better visual appearance.
- **Error Handling**: Displays an error message if the expression is invalid.
- **Clear Function**: Allows users to clear the current input.
- **Responsive Layout**: Buttons and entry field are organized in a responsive grid layout.

## Installation

Ensure you have Python installed on your machine. This script uses the Tkinter library, which is included with Python's standard library, so no additional installation is required.

## Usage

1. **Run the Script**: Save the code into a file named `calculator.py` and run it using Python:
    ```bash
    python calculator.py
    ```

2. **Using the Calculator**:
    - **Input Numbers and Operators**: Click on the number and operator buttons to input values and operators.
    - **Evaluate Expression**: Click the `=` button to compute the result.
    - **Clear Input**: Click the `C` button to clear the current input.

## Code Explanation

- **Main Window**: The application window is created with a title "Calculator" and a fixed size of 350x500 pixels. The background color is set to a dark grey.

- **Entry Widget**: An entry widget is used to display the current expression and result. It is styled with a custom font and dark background.

- **Buttons**: A grid of buttons is created to represent digits, operators, and functional commands. Each button is styled with a distinct color and has a specific command associated with it:
    - **Digits and Operators**: Append values to the current expression.
    - **`C` Button**: Clears the input field.
    - **`=` Button**: Evaluates the expression and displays the result or an error message.

- **Name Label**: A label displaying the name "Allmin" is included for personalization.

## Example

When the script is executed, a window with a calculator interface will appear. You can perform basic arithmetic operations by clicking on the buttons. The result will be displayed in the entry field after pressing the `=` button.

## Output

Here is a screenshot of the calculator application:

![output](https://github.com/user-attachments/assets/c6d7320d-595a-4ac8-b7c6-c554502a7d1f)


## Acknowledgments

- This project uses the Tkinter library, which is included with Python and provides a simple way to create graphical user interfaces.
- Special thanks to the Python community for their extensive documentation and support.

For any issues or questions, feel free to open an issue or contact me.
