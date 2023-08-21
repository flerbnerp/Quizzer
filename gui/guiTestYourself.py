import tkinter as tk
import random
from selectionLogic import get_weighted_question
from mainLoopDefines import get_md_content, update_score
import os
import threading

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
        
        # Create a Canvas widget to hold the question frame
        self.canvas = tk.Canvas(self, bg='black', bd=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2, sticky="nsew")
        # Create a Frame widget inside the Canvas
        self.question_frame = tk.Frame(self.canvas, bg='black')
        self.canvas.create_window((0, 0), window=self.question_frame, anchor="nw")
        # Create a Label widget inside the Frame
        self.question_field = "DEBUG, QUESTION LOOP IS BROKEN"  # Variable to hold the question label text
        self.question_label = tk.Label(self.question_frame, text="", wraplength=500, bg='black', fg='white')
        self.question_label.pack(side="top", anchor="w")
        # Create a vertical scrollbar
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=2, sticky="ns")
        # Configure canvas to use the scrollbar
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        # Bind an event to update the canvas scrolling when the question_label's size changes
        self.question_label.bind("<Configure>", self.update_scroll_region)
        
        # Input field
        self.input_field = tk.Text(self, bg='white', height=3, wrap=tk.WORD)  # Height is set to 3 lines and text will wrap at word boundaries
        self.input_field.grid(row=1, column=0, sticky="nsew")
        # Bindings for the input field
        self.input_field.bind('<Return>', self.on_enter_pressed)
        self.input_field.bind('<Shift-Return>', self.insert_linebreak)

        # Submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_answer)
        self.submit_button.grid(row=1, column=1)
        
        # Create a StringVar to store user input
        self.user_input_var = tk.StringVar()
        self.user_input_var.set("")  # Initialize to empty string
        
        # Start the question loop in a separate thread
        self.question_thread = threading.Thread(target=self.question_loop)
        self.question_thread.daemon = True  # Allow the thread to be terminated when the GUI closes
        self.question_thread.start()
    
    def update_scroll_region(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_enter_pressed(self, event=None):
        self.submit_button.invoke()
        return "break"  # Stops the event from propagating

    def insert_linebreak(self, event=None):
        self.input_field.insert(tk.INSERT, '\n')
        return "break"  # Stops the event from propagating

    def submit_answer(self):
        self.user_input_var.set(self.input_field.get("1.0", tk.END).strip())
        self.input_field.delete("1.0", tk.END)
    # Question loop
    def question_loop(self):
        # Main loop
        main_list = []  # A list to store the questions for the current batch
        user_input = self.user_input_var.get().strip().lower()
        
        while True:
            # If main_list is empty, repopulate it
            if not main_list:
                main_list = get_weighted_question()

            # Get a random question and its answer from the main list
            idx = random.randint(0, len(main_list) - 1)
            question, answer, filename = main_list.pop(idx)

            # 2. Prompt the user with the question
            self.question_field = question
            self.question_label.config(text=self.question_field)
            self.master.wait_variable(self.user_input_var)
            # Concatenate user input to the question label's current text
            self.question_field = self.question_field + "\n\nYour Answer: " + self.user_input_var.get()
            self.question_label.config(text=self.question_field)
            
            # 3. Display the correct answer
            if answer.endswith(".md"):
                md_content = get_md_content(answer)
                answer_text = f"Correct Answer:\n{md_content}\n"
            else:
                answer_text = f"Correct Answer: {answer}\n"
            # Concatenate the answer to the question_label field
            self.question_field = self.question_field + "\n\n" + answer_text
            self.question_field = self.question_field + "\n\nQuestion Correct? Enter yes or no:"
            self.question_label.config(text=self.question_field)
            # 4. Prompt the user to continue
            while True:
                self.master.wait_variable(self.user_input_var)
                user_input = self.user_input_var.get().strip().lower()
                if user_input == "yes":
                    update_score(question, filename, correct=True)
                    break
                elif user_input == "no":
                    update_score(question, filename, correct=False)
                    break
                elif user_input == "debug":
                    break
                else:
                    self.question_field = self.question_field + "\n\nInvalid input. Please enter 'Yes' or 'No'."
                    self.question_label.config(text=self.question_field)