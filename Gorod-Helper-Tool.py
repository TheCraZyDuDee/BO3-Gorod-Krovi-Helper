import os
import tkinter as tk
from tkinter import ttk
import webbrowser

# Initialize counter
counter = 0

# Create a function to focus to the root window
def on_combobox_selected(event):
    root.focus()

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
    button['text'] = f"{location} ({counter})"
    button['state'] = "disabled"
    if counter == 6:
        disable_all_buttons()

# Create a function to reset all buttons
def reset():
    global counter
    counter = 0
    for i, button in enumerate(buttons):
        button['text'] = locations[i]
        button['state'] = "normal"
    # Reset the dropdown menus
    start_var.set("Green Light Valve")
    end_var.set("Pink Cylinder Valve")
    # Clear the text widget
    result_text.delete(1.0, tk.END)

# Function to open your GitHub page
def open_github(event):
    webbrowser.open('https://github.com/TheCraZyDuDee/BO3-Gorod-Krovi-Helper')

# Define the combinations
combinations = {
    ("Armory", "Tank Factory"): {"Armory": 3, "Dept. Store(3rd Floor)": 2, "Infirmary": 3, "Dragon Command": 1, "Supply Depot": 3, "Tank Factory": "Cylinder Location"},
    ("Armory", "Dept. Store"): {"Armory": 1, "Supply Depot": 3, "Tank": 1, "Infirmary": 1, "Dragon Command": 2, "Dept. Store": "Cylinder Location"},
    ("Armory", "Dragon Command"): {"Armory": 3, "Dept. Store": 2, "Infirmary": 2, "Tank Factory": 2, "Supply Depot": 1, "Dragon Command": "Cylinder Location"},
    ("Armory", "Supply Depot"): {"Armory": 2, "Tank Factory": 1, "Infirmary": 1, "Dept. Store": 3, "Dragon Command": 1, "Supply Depot": "Cylinder Location"},
    ("Armory", "Infirmary"): {"Armory": 2, "Tank Factory": 2, "Supply Depot": 1, "Dragon Command": 2, "Dept. Store": 2, "Infirmary": "Cylinder Location"},
    ("Dept. Store", "Armory"): {"Dept. Store": 3, "Dragon Command": 3, "Infirmary": 2, "Tank Factory": 2, "Supply": 2, "Armory": "Cylinder Location"},
    ("Dept. Store", "Dragon Command"): {"Dept. Store": 2, "Infirmary": 2, "Tank Factory": 3, "Armory": 1, "Supply Depot": 1, "Dragon Command": "Cylinder Location"},
    ("Dept. Store", "Supply Depot"): {"Dept. Store": 1, "Armory": 2, "Tank Factory": 1, "Infirmary": 3, "Dragon Command": 3, "Supply Depot": "Cylinder Location"},
    ("Dept. Store", "Infirmary"): {"Dept. Store": 1, "Armory": 2, "Tank Factory": 2, "Supply Depot": 1, "Dragon Command": 3, "Infirmary": "Cylinder Location"},
    ("Dept. Store", "Tank Factory"): {"Dept. Store": 2, "Infirmary": 3, "Dragon Command": 1, "Supply Depot": 2, "Armory": 2, "Tank Factory": "Cylinder Location"},
    ("Dragon Command", "Supply Depot"): {"Dragon Command": 2, "Dept. Store": 2, "Infirmary": 2, "Tank Factory": 3, "Armory": 1, "Supply Depot": "Cylinder Location"},
    ("Dragon Command", "Infirmary"): {"Dragon Command": 1, "Supply Depot": 3, "Tank Factory": 3, "Armory": 3, "Dept. Store": 2, "Infirmary": "Cylinder Location"},
    ("Dragon Command", "Tank Factory"): {"Dragon Command": 3, "Infirmary": 1, "Dept. Store": 1, "Armory": 1, "Supply Depot": 3, "Tank Factory": "Cylinder Location"},
    ("Dragon Command", "Dept. Store"): {"Dragon Command": 1, "Supply Depot": 2, "Armory": 2, "Tank Factory": 1, "Infirmary": 1, "Dept. Store": "Cylinder Location"},
    ("Dragon Command", "Armory"): {"Dragon Command": 1, "Supply Depot": 3, "Tank Factory": 1, "Infirmary": 1, "Dept. Store": 1, "Armory": "Cylinder Location"},
    ("Supply Depot", "Infirmary"): {"Supply Depot": 3, "Tank Factory": 3, "Armory": 3, "Dept. Store": 3, "Dragon Command": 3, "Infirmary": "Cylinder Location"},
    ("Supply Depot", "Tank Factory"): {"Supply Dept": 2, "Armory": 3, "Dept. Store": 3, "Dragon Command": 3, "Infirmary": 2, "Tank Factory": "Cylinder Location"},
    ("Supply Depot", "Dragon Command"): {"Supply Depot": 3, "Tank Factory": 3, "Armory": 3, "Dept. Store": 2, "Infirmary": 3, "Dragon Command": "Cylinder Location"},
    ("Supply Depot", "Dept. Store"): {"Supply Depot": 2, "Armory": 2, "Tank Factory": 1, "Infirmary": 3, "Dragon Command": 2, "Dept. Store": "Cylinder Location"},
    ("Supply Depot", "Armory"): {"Supply Depot": 3, "Tank Factory": 1, "Infirmary": 3, "Dragon Command": 2, "Dept. Store": 1, "Armory": "Cylinder Location"},
    ("Infirmary", "Tank Factory"): {"Infirmary": 3, "Dragon Command": 2, "Dept. Store": 1, "Armory": 1, "Supply Depot": 3, "Tank Factory": "Cylinder Location"},
    ("Infirmary", "Supply Depot"): {"Infirmary": 3, "Dragon Command": 2, "Dept. Store": 1, "Armory": 2, "Tank Factory": 2, "Supply Depot": "Cylinder Location"},
    ("Infirmary", "Dragon Command"): {"Infirmary": 2, "Tank Factory": 2, "Supply Depot": 2, "Armory": 2, "Dept. Store": 3, "Dragon Command": "Cylinder Location"},
    ("Infirmary", "Dept. Store"): {"Infirmary": 3, "Dragon Command": 1, "Supply Depot": 3, "Tank Factory": 3, "Armory": 3, "Dept. Store": "Cylinder Location"},
    ("Infirmary", "Armory"): {"Infirmary": 2, "Tank Factory": 2, "Supply Depot": 1, "Dragon Command": 2, "Dept. Store": 1, "Armory": "Cylinder Location"},
    ("Tank Factory", "Infirmary"): {"Tank Factory": 2, "Supply Depot": 2, "Armory": 2, "Dept. Store": 3, "Dragon Command": 3, "Infirmary": "Cylinder Location"},
    ("Tank Factory", "Supply Depot"): {"Tank Factory": 1, "Infirmary": 3, "Dragon Command": 2, "Dept. Store": 1, "Armory": 1, "Supply Depot": "Cylinder Location"},
    ("Tank Factory", "Dragon Command"): {"Tank Factory": 1, "Infirmary": 1, "Dept. Store": 1, "Armory": 1, "Supply Depot": 1, "Dragon Command": "Cylinder Location"},
    ("Tank Factory", "Dept. Store"): {"Tank Factory": 1, "Infirmary": 3, "Dragon Command": 1, "Supply Depot": 2, "Armory": 3, "Dept. Store": "Cylinder Location"},
    ("Tank Factory", "Armory"): {"Tank Factory": 1, "Infirmary": 1, "Dept. Store": 3, "Dragon Command": 1, "Supply Depot": 2, "Armory": "Cylinder Location"}
}

def get_settings():
    # Get the start and end points from the dropdown menus
    start_point = start_var.get()
    end_point = end_var.get()

    # Get the correct settings for the valves
    settings = combinations.get((start_point, end_point))

    if settings is not None:
        result = f"The settings for the valves are:\n"
        for location, setting in settings.items():
            result += f"{location}: {setting}\n"
    else:
        result = "Invalid start or end point."

    # Display the result in the text widget
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# Get the directory of the script or executable
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the icon file
icon_path = os.path.join(dir_path, 'gorod.ico')

# Create main window
root = tk.Tk()
root.iconbitmap(icon_path)
root.title("Gorod Helper Tool")
root.geometry("635x320")
root.resizable(False, False)

# Create label
label = tk.Label(root, text="Select Locations in order to remember them")
label.place(x=9, y=15)

# Create second label
label2 = tk.Label(root, text="Select the appropriate Valves in the Dropdown Menus below")
label2.place(x=307, y=15)

# Create version label
label3 = tk.Label(root, text="v0.0.3")
label3.place(x=590, y=290)

# Create the GitHub link label
github_link = tk.Label(root, text="Github", fg="blue", cursor="hand2")
github_link.place(x=7, y=290)  # Adjust the coordinates as needed
github_link.bind("<Button-1>", open_github)

# Create buttons
locations = ["Tank Factory", "Dragon Command", "Infarmy", "Armory", "Supply Depot", "Dept. Store"]
buttons = []
button_y_coordinate = 50  # Initial y-coordinate for the first button
for i, location in enumerate(locations):
    button = tk.Button(root, text=location, command=lambda loc=location, i=i: update_button(buttons[i], loc), width=39, height=1)
    button.place(x=10, y=button_y_coordinate)  # Place the button at the specified coordinates
    buttons.append(button)
    button_y_coordinate += 30  # Increase the y-coordinate for the next button

# Create reset button
reset_button = tk.Button(root, text="Reset", width=6, height=1, command=reset)
reset_button.place(x=7, y=250)

# Create the dropdown menus
start_var = tk.StringVar()
end_var = tk.StringVar()
start_var.set("Green Light Valve")
end_var.set("Pink Cylinder Valve")
start_menu = ttk.Combobox(root, state="readonly", textvariable=start_var, values=list(set([key[0] for key in combinations.keys()])))
end_menu = ttk.Combobox(root, state="readonly", textvariable=end_var, values=list(set([key[1] for key in combinations.keys()])))
start_menu.place(x=310, y=50)
end_menu.place(x=465, y=50)

start_menu.bind("<<ComboboxSelected>>", on_combobox_selected)
end_menu.bind("<<ComboboxSelected>>", on_combobox_selected)

# Create the button
button = tk.Button(root, text="Get Settings", command=get_settings)
button.place(x=310, y=80)

# Create the text widget
result_text = tk.Text(root, width=37, height=10)
result_text.place(x=310, y=114)

# Run the application
root.mainloop()
