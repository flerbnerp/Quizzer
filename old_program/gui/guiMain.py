
import tkinter as tk
from . import guiButtons  # Assuming guiMain.py and guiButtons.py are in the same directory

def start_gui():
    root = tk.Tk()
    root.title("Quizzer GUI")
    # Set the window size: width x height
    root.geometry("1200x800")
    button_height = 50  # Example height
    root.grid_rowconfigure(0, minsize=button_height)  # Set height for row 1
    root.grid_rowconfigure(1, weight=1)  # Let row 2 take up the remaining space
    root.grid_rowconfigure(2, weight=1)  # Let row 3 (index 2) take up the remaining space
    root.grid_columnconfigure(0, weight=1)  # Make the first column expandable
    root.grid_columnconfigure(1, weight=1)  # Make the second column expandable
    root.grid_columnconfigure(2, minsize=button_height)

    # Create the buttons using the function from guiButtons module
    quit_button, test_button = guiButtons.create_buttons(root)

    # Now, you can link the test_button's command to some other function if needed
    # For example: test_button["command"] = some_function_name

    root.mainloop()
