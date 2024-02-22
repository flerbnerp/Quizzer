import json
import random
from datetime import datetime, timedelta
import os

def populate_question_list():
    with open("settings.json", "r") as f:
        settings = json.load(f)
    quiz_length = settings["quiz_length"]
    sorted_questions = []
    # load in config.json into memory
    with open("questions.json", "r") as f:
        questions = json.load(f)
    # Check function that removes questions from master list if the next_revision_due date is not with 24 hours of now    
    # If overdue or due within 24 hours, question is appended to the sorted_questions variable
    # This check function is required for an edge case where only a couple questions exist under a given subject, without removing questions outside of the normal 
    # due date range, questions risk being repeated over and over and over again even though they may be due for revision much later than today's date + 24 hours.
    for question in questions:
        question["next_revision_due"] = datetime.strptime(question["next_revision_due"], "%Y-%m-%d %H:%M:%S")
        if question["next_revision_due"] <= (datetime.now() + timedelta(hours=24)):
            sorted_questions.append(question)
    # Sort question objects by next_revision_due key value
    sorted_questions = sorted(questions, key=lambda x: x['next_revision_due'])
    
    
    
    # Initialize question list to be filled
    question_list = []

    # Fill question list with desired number of questions for practice exam, based on the questions inside the sorted_questions variable, not the master database
    for i in sorted_questions:
        if len(question_list) == quiz_length: #We break the loop once we have the desired number of questions
            break
        else:
            question_list.append(i)
            
        # while loop for questions? provide a counter for each subject to be filled, stop adding questions of that type once the counter = the weight value?
        # when a question is added from sorted questions pop that question from the list
        
        
    # for i in questions:
    #     print(f"{i}\n")
    random.shuffle(question_list) # ensures there is some level of randomization, so users don't notice this is just a cycling list
    question_list = question_list[::-1] # Reverse the list
    random.shuffle(question_list) # Shuffle it again
    return question_list
