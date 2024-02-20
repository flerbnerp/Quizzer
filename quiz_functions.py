import json
import random
import datetime
import os

def populate_question_list():
    questions = []
    # load in config.json into memory
    with open("questions.json", "r") as f:
        existing_data = json.load(f)
    # extract all question objects
    for dictionary in existing_data:
        if dictionary["type"] == "question":
            dictionary["next_revision_due"] = datetime.datetime.strptime(dictionary["next_revision_due"], "%Y-%m-%d %H:%M:%S")
            questions.append(dictionary)
    # Sort question objects by next_revision_due key value
    questions = sorted(questions, key=lambda x: x['next_revision_due'])
    # Initialize question list and desired number of questions for practice exam
    question_list = []

    # Fill question list with desired number of questions for practice exam
    for i in questions:
        if len(question_list) == 35:
            break
        else:
            question_list.append(i)
        
    # for i in questions:
    #     print(f"{i}\n")
    random.shuffle(question_list) # ensures there is some level of randomization, so users don't notice this is just a cycling list
    question_list = question_list[::-1] # Reverse the list
    random.shuffle(question_list) # Shuffle it again
    return question_list