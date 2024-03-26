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
from initialize import initialize_quizzer
from scoring_algorithm import update_score
from quiz_functions import populate_question_list
from stats import print_stats, completed_quiz,print_and_update_revision_streak_stats
from settings import update_setting, get_subjects
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

# example (I'll be reading from this example for the update score call)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
	if q == "test" and item_id == 5:
		response = "Ooga booga!"
	else:
		response = "try again"
	return response

@app.get("/update_score/{status, file_name}")
def question_answer_update_score(status: str, file_name: str):
    print(file_name)
    decoded_file_name = file_name
    # decoded_file_name = unquote(file_name)
    # print(decoded_file_name)
    response = f"{decoded_file_name}, {file_name}"
    file_name = decoded_file_name
    if status == "correct":
        update_score(status, file_name)
    elif status == "incorrect":
        update_score(status, file_name)
    else:
        response = "Please enter a valid status, 'correct' or 'incorrect'"
    return response

@app.get("/update_setting/{key, value}")
def update_a_setting_value(key=str, value=str):
	print(key)
	print(value)
	response = update_setting(key, value)
	return response

@app.get("/get_media_path/{media_file_name}")
def return_file_path(media_file_name=str):
    '''Takes a file name string as input, returns the location of the media'''
    print(media_file_name)
    with open("media_paths.json", "r") as f:
        media_paths = json.load(f)
    print(len(media_paths["file_paths"]))
    for path in media_paths["file_paths"]: # Iterate through the existing media
        if str(path).endswith(media_file_name):
            return path		

@app.get("/initialize_quizzer")
def initialization(): # This function will contain all the initialization functions from various modules:
	initialize_quizzer()

@app.get("/completed_quiz")
def update_completed_quiz_stat():
	'''
	Tells Quizzer that a quiz is completed and to update stats.json, among other general stats
	'''
	completed_quiz()
 
@app.get("/get_subjects")
def api_get_subjects():
	'''Returns a set of all subjects in quizzer'''
	subjects = get_subjects()
	return subjects

@app.get("/get_subject_settings")
def get_subject_settings():
    root = "http://127.0.0.1:8000/"
    settings_menu = True
    subject_settings = {}
    with open("settings.json", "r") as f:
        settings = json.load(f)
    query = root + "get_subjects"
    subjects = get_subjects()
    subjects = list(subjects)
    subjects = sorted(subjects)
    for i in range(0, (len(subjects)-1)):
        for key, value in settings.items():
            if subjects[i] in key:
                subject_settings[key] = value
    return subject_settings
############################################################
# One api call for each stat that could be displayed
# One general api call that returns a list of all stats in string (with line breaks)
@app.get("/get_average_questions_per_day")
def get_average_questions_per_day():
    # Make sure to update stats.json before returning data
    print_and_update_revision_streak_stats()
    with open("stats.json", "r") as f:
        stats = json.load(f)
    average_questions = stats["average_questions_per_day"]
    return average_questions