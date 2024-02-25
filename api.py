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
from quiz_functions import populate_question_list


app = FastAPI()

@app.get("/")
def read_root():
    data = {"Hello": "World"}
    return data

@app.get("/stats")
def return_stats():
    with open("stats.json", "r") as f:
        stats_data = json.load(f)
    stats_data["average quiz length"] = sum(stats_data["quiz_lengths"]) / len(stats_data["quiz_lengths"])
    return stats_data

@app.get("/populate_quiz")
def return_question_list():
    question_list, sorted_questions = populate_question_list()

# example
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if q == "test" and item_id == 5:
        response = "Ooga booga!"
    else:
        response = "try again"
    return response