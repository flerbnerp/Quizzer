import tkinter as tk
from tkinter import ttk
def create_question_config_interface(master):
    question_config_interface(master)
      
class question_config_interface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='black')
        self.master = master
        self.grid(row=1, rowspan=2, column=0, columnspan=3, sticky="nsew")
        # Row configurations
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0) 
        self.grid_rowconfigure(3, weight=1)
        # Column configurations
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_columnconfigure(7, weight=0)
        
        # Static labels
        category_label = tk.Label(self, text="Category:", bg='black', fg='white')
        category_label.grid(row=0, column=0, sticky='w')
        # Category dropdown menu (to be populated later)
        category_var = tk.StringVar()
        category_dropdown = ttk.Combobox(self, textvariable=category_var, state='readonly')
        category_dropdown.grid(row=0, column=1, columnspan=2, sticky='w')
        # Add button
        add_button = tk.Button(self, text="Add")
        add_button.grid(row=0, column=6, columnspan=2, sticky='w')
        # Labels for properties
        properties_labels = ["Question", "Answer", "Correct #", "Wrong #", "Total #", "Edit", "Delete"]
        for idx, label_text in enumerate(properties_labels):
            label = tk.Label(self, text=label_text, bg='black', fg='white')
            label.grid(row=2, column=idx, sticky='w')
        # Scrollable area for listing questions and properties (starting from row 4)
        scrollable_area = tk.Frame(self, bg='black')
        scrollable_area.grid(row=3, column=7)
        scrollbar = tk.Scrollbar(scrollable_area, orient="vertical")
        scrollbar.pack(side="right", fill="n")