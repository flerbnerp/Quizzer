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
from stats import print_stats, completed_quiz
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
    