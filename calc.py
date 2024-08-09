import tkinter as tk
from tkinter import font

# Function to update the expression in the input field
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to clear the input field
def clear_entry():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Creating the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.configure(bg='#2e2e2e')

# Define a custom font
custom_font = font.Font(family="Arial", size=18)

# Entry widget for displaying calculations
entry = tk.Entry(root, font=custom_font, bg='#333', fg='#fff', borderwidth=2, relief="solid")
entry.pack(padx=20, pady=20, fill=tk.BOTH)

# Button frame
button_frame = tk.Frame(root, bg='#2e2e2e')
button_frame.pack()

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Create buttons and add them to the button frame
for row in buttons:
    button_row = tk.Frame(button_frame, bg='#2e2e2e')
    button_row.pack()
    for button in row:
        if button == 'C':
            b = tk.Button(button_row, text=button, font=custom_font, width=5, height=2, bg='#ff4d4d', fg='#fff', command=clear_entry)
        elif button == '=':
            b = tk.Button(button_row, text=button, font=custom_font, width=5, height=2, bg='#4dff4d', fg='#fff', command=evaluate_expression)
        else:
            b = tk.Button(button_row, text=button, font=custom_font, width=5, height=2, bg='#4d4dff', fg='#fff', command=lambda btn=button: click_button(btn))
        b.pack(side=tk.LEFT, padx=5, pady=5)

# Label for displaying the name
name_label = tk.Label(root, text="Allmin", font=("Arial", 24), bg='#2e2e2e', fg='#fff')
name_label.pack(pady=10)

# Run the main loop
root.mainloop()
