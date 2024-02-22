import json
import random
from datetime import datetime, timedelta
from settings import get_subjects
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
        if question["next_revision_due"] <= (datetime.now() + timedelta(hours=24)) and question["subject"] != None:
            sorted_questions.append(question)
    # Sort question objects by next_revision_due key value
    sorted_questions = sorted(questions, key=lambda x: x['next_revision_due'])
    temp_list = []
    for question in sorted_questions:
        if question["subject"] == None:
            print(question["file_name"])
        elif question["subject"] != None:
            temp_list.append(question)
    sorted_questions = temp_list
    
    # Initialize question list to be filled
    question_list = []

    # Fill question list with desired number of questions for practice exam, based on the questions inside the sorted_questions variable, not the master database
    subject_set = get_subjects()
    question_list_is_filled = False
    subjects = list(subject_set)
    subjects_list = []
    subjects_by_count = {}
    while question_list_is_filled == False:
        print("--------------------------------")
        if question_list_is_filled == True:
            break
        # Gather all questions in a list so we can count total questions by subject
        for question in sorted_questions:
            if question["subject"] is not None:
                subjects_list.extend(question["subject"])
        # Get count of all questions
        for subject in subjects:
            count = subjects_list.count(subject)
            subjects_by_count[subject] = count
            
        # Iterate through each subject and add questions based on weighting
        adding_questions = True
        for key, value in subjects_by_count.items():
            questions_to_add_to_list = settings[f"subject_{key}_weight"]
            
            for question in sorted_questions:
                if questions_to_add_to_list <= 0:
                    break
                if len(question_list) == quiz_length:
                    question_list_is_filled = True
                    break
                # check setting weight against total questions for subject:
                if value < settings[f"subject_{key}_weight"]:
                    print("value is less than desired amount, skipping subject")
                    break
                if value >= settings[f"subject_{key}_weight"]: # If there are enough we need to fill them
                    if key in question["subject"]:                    
                        question_list.append(question)
                        print(f"added 1 question from {key}")
                        print(f"question is list {len(question_list)} questions long")
                        questions_to_add_to_list -= 1
                        index = sorted_questions.index(question)
                        sorted_questions.pop(index)
                            
                else:
                    print("oops big loop went wrong?")

                                
        # while loop for questions? provide a counter for each subject to be filled, stop adding questions of that type once the counter = the weight value?
        # when a question is added from sorted questions pop that question from the list
        
        
    # for i in questions:
    #     print(f"{i}\n")
    random.shuffle(question_list) # ensures there is some level of randomization, so users don't notice this is just a cycling list
    question_list = question_list[::-1] # Reverse the list
    random.shuffle(question_list) # Shuffle it again
    print(len(question_list))
    print(type(question_list))
    for i in question_list:
        print(f"{i['subject']}")
    return question_list