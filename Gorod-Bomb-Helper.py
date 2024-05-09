import os
import tkinter as tk

# Initialize counter
counter = 0

# Create a function to disable all buttons
def disable_all_buttons():
    for button in buttons:
        button["state"] = "disabled"

# Create a function to enable all buttons
def enable_all_buttons():
    for button in buttons:
        button["state"] = "normal"

# Create a function to update button state and text
def update_button(button, location):
    global counter
    counter += 1
    label['text'] = f"{location} - {counter}"
    button['text'] = f"{location} ({counter})"
    button['state'] = "disabled"
    if counter == 6:
        disable_all_buttons()

# Create a function to reset all buttons
def reset():
    global counter
    counter = 0
    label['text'] = "Select Locations in order to remember them"
    for i, button in enumerate(buttons):
        button['text'] = locations[i]
        button['state'] = "normal"

# Get the directory of the script or executable
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the icon file
icon_path = os.path.join(dir_path, 'gorod.ico')

# Create main window
root = tk.Tk()
root.iconbitmap(icon_path)
root.title("Gorod Bomb Helper")
root.geometry("300x320")

# Add a label at the top with a large amount of padding
top_label = tk.Label(root, text="")
top_label.pack(pady=12)  # Adjust this value to place the buttons lower or higher

# Create label
label = tk.Label(root, text="Select Locations in order to remember them")
label.place(x=9, y=15)

# Create version label
vlabel = tk.Label(root, text="v0.0.1")
vlabel.place(x=9, y=290)

# Create buttons
locations = ["Tank Factory", "Dragon Command", "Infarmy", "Armory", "Supply Depot", "Dept. Store"]
buttons = []
button_width = 39
button_height = 1
for i, location in enumerate(locations):
    button = tk.Button(root, text=location, command=lambda loc=location, i=i: update_button(buttons[i], loc), width=button_width, height=button_height)
    button.pack(pady=2)  # Add vertical padding
    buttons.append(button)

# Create reset button
reset_button = tk.Button(root, text="Reset", width=6, height=1, command=reset)
reset_button.place(x=7, y=250)

# Run the application
root.mainloop()
