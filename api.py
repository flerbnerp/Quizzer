# Installation of quizzer:
# pip3 install starlette
# pip3 install uvicorn
# pip install "uvicorn[standard]"
# pip install pydantic
# pip install fastapi

#How to run the server component
from typing import Union
from fastapi import FastAPI
import json
from initialize import initialize_or_update_json, initialize_master_question_list
from scoring_algorithm import generate_revision_schedule, update_score
from quiz_functions import populate_question_list
from stats import initialize_stats_json, print_stats, completed_quiz
from settings import initialize_settings_json, initialize_settings_json_keys
# To start API 

app = FastAPI()

@app.get("/")
def read_root():
    data = {"Hello": "World"}
    return data

@app.get("/stats")
def return_stats():
    stats_list = print_stats()
    return {"stat_list": stats_list}

@app.get("/populate_quiz")
def return_question_list():
    question_list, returned_sorted_questions = populate_question_list()
    return {"question_list": question_list, "sorted_questions": returned_sorted_questions}

# example
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if q == "test" and item_id == 5:
        response = "Ooga booga!"
    else:
        response = "try again"
    return response

@app.get("/initialize_quiz")
def initialize_quizzer(): # This function will contain all the initialization functions from various modules:
    def initialization():
    # Scan provided file directory for all .md files and store data in config.json
        initialize_or_update_json() 
        initialize_master_question_list()
        generate_revision_schedule() # generates the revision schedule that will determine when notes will be served to the user
        initialize_settings_json()
        initialize_settings_json_keys()
        initialize_stats_json()
    vault_path = "/home/karibar/Documents/Education"
    error = False # for use if the user enters an invalid input
    #################################################################################################################################################
    ## Calling Initalization functions
    config_file_exists = False
    questions_file_exists = False
    try:
        with open("config.json", "r") as f:
            config_file_exists = True
    except:
        pass
    try:
        with open("questions.json", "r") as f:
            questions_file_exists = True
    except:
        pass
    if (config_file_exists == False) or (questions_file_exists == False):
        print("Missing files, long initialization in progress")
        initialization()
        initialization()
        initialization()
    else:
        initialization()