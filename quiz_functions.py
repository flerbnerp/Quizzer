import json
import random
import datetime
import os
def populate_question_list_legacy():
    questions = []
    with open("config.json", "r") as f:
        database = json.load(f)
    for i in database:
        if i["type"] == "question":
            questions.append(i)
    question_list = [] # empty the question list, prevents need to pass question_list into the function
    number_of_questions = 25
    len_questions = len(questions) - 1
    while len(question_list) < number_of_questions: # populates the difference betwene number_of_concepts and number_of_questions if 18 and 20, this populates 2 questions into the list
        rand = random.randint(0, len_questions)
        question_list.append(questions[rand])
    random.shuffle(question_list) # Shuffles the order of the list, without this, only concept notes will be presented then only questions.
    return question_list

def populate_question_list():
    questions = []
    # load in config.json into memory
    with open("config.json", "r") as f:
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
        if len(question_list) == 25:
            break
        else:
            question_list.append(i)
        
    # for i in questions:
    #     print(f"{i}\n")
    random.shuffle(question_list) # ensures there is some level of randomization, so users don't notice this is just a cycling list
    return question_list