import tkinter as tk
import random
from initialize import initialize_education_directory
from initializeFilePath import construct_filepaths_directory
from mainLoopDefines import get_md_content, update_score
from selectionLogic import get_weighted_question

class TestYourself(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='black')
        self.master = master
        self.grid(row=1, rowspan=2, column=0, columnspan=3, sticky="nsew")
        # Row configurations
        self.grid_rowconfigure(0, weight=9)  # 90% of the height for the question
        self.grid_rowconfigure(1, weight=1)  # 10% of the height for the input field and submit button
        
        # Column configurations
        self.grid_columnconfigure(0, weight=1)  # 1st column that will take up half the width
        self.grid_columnconfigure(1, weight=0)  # 2nd column
        
        # Question prompt label spanning both columns
        self.question_label = tk.Label(self, text="Question will go here.", wraplength=500)  # wraplength can be adjusted
        self.question_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Input field
        self.input_field = tk.Text(self, bg='white', height=3, wrap=tk.WORD)  # Height is set to 3 lines and text will wrap at word boundaries
        self.input_field.grid(row=1, column=0, sticky="nsew")
        
        # Bindings for the input field
        self.input_field.bind('<Return>', self.on_enter_pressed)
        self.input_field.bind('<Shift-Return>', self.insert_linebreak)

        # Submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_answer)
        self.submit_button.grid(row=1, column=1)
        
    def on_enter_pressed(self, event=None):
        self.submit_button.invoke()
        return "break"  # Stops the event from propagating

    def insert_linebreak(self, event=None):
        self.input_field.insert(tk.INSERT, '\n')
        return "break"  # Stops the event from propagating

    def submit_answer(self):
        # Get the text from the input field
        answer_text = self.input_field.get("1.0", tk.END).strip()  # "1.0" refers to the start of the text widget, and tk.END refers to the end of the widget.

        # Set the text of the question label to the answer text
        self.question_label.config(text=answer_text)

        # Optionally, clear the input field if desired
        self.input_field.delete("1.0", tk.END)