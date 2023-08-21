import tkinter as tk
from .guiTestYourself import TestYourself


def create_test_interface(master):
    test_frame = TestYourself(master)
def create_buttons(master):
    """
    Create and place the buttons on the master window/frame
    """
    # Create a header frame with a black background
    header_frame = tk.Frame(master, bg='black')
    header_frame.grid(row=0, column=0, columnspan=2, sticky='ew')

    # Adjust column weights of the header frame so the buttons fill it horizontally
    header_frame.columnconfigure(0, weight=1)  # Test Yourself button will expand as needed
    header_frame.columnconfigure(1, weight=0)  # Quit button will use only the space it needs

    # Quit button
    quit_button = tk.Button(master, text="Quit", command=master.quit)
    quit_button.grid(row=0, column=0, sticky='w')  # 'e' means align right
    # Test Yourself button
    test_button = tk.Button(master, text="Test Yourself", command=lambda: create_test_interface(master))  # We will bind functionality to this button later
    test_button.grid(row=0, column=1, sticky='w')  # 'w' means align left

    return quit_button, test_button
