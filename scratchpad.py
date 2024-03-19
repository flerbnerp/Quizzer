from urllib.parse import quote, unquote
from initialize import initialize_quizzer
import json
import re
import yaml
from datetime import datetime
import math

def parse_yaml_string(yaml_string):
    parsed_data = {}
    list_value = []
    parsing_multiline_value = False
    key = "error"
    for line in yaml_string.split("\n"):
        # Attempting to build function methodically with if else statements
        
        # My first question, is the line I'm looking at a property line or not?
        if line.startswith(" -") and (":" not in line):
            property_line = False
        else:
            property_line = True
        
        # if it's a property line, does it have a value attached? Grab the key, its a property
        if property_line and len(list_value) != 0:
            #Means we have finished iterating through a multiline property
            parsed_data[key] = list_value
            list_value = []
        if property_line:
            index = line.find(":")
            key = line[:index]
            split_line = line.strip().split(":")
            if len(split_line) == 2:
                multiline = True
                split_line[1] = split_line[1].strip()
                parsed_data[key] = split_line[1]
            print(key)
        elif not property_line: # We should have a key loaded in memory, but this is not the case
            working_line = line.strip()
            index = working_line.find("-") + 1
            working_line = working_line[index:]
            working_line = working_line.strip()
            print(f"working_line:{working_line}")
            list_value.append(working_line)
            
    del parsed_data["error"]
    return parsed_data

# Example usage
yaml_string = """
type: book_note
sub-type:
  - textbook
Author:
  - Jennifer Niederst Robbins
Date: 
audience: Students
previous-chapter: "[[Learning Web Design - Transitions, Transforms, and Animation - 18]]"
"chapter #": "19"
"page #": "547"
next-chapter: "[[Learning Web Design - Modern Web Development Tools - 20]]"
subject:
  - computer_science: Weird value
  - web_design: weird value
related:
  - "[[Learning_Web_Design.pdf]]"
progress: 
due_date: 2024-03-26
"""
# parsed_data = parse_yaml_string(yaml_string)
# print(parsed_data)