import json
import random
from constants import QA_FILE

def get_md_content(file_name):
    """Retrieve the content of a markdown file based on its filename using config.json."""
    with open('config.json', 'r') as file:
        config = json.load(file)
        filepaths = config.get("filepaths", {})
        path_to_md = filepaths.get(file_name)
        
        if path_to_md:
            with open(path_to_md, 'r') as md_file:
                return md_file.read()
        else:
            return "Error: Markdown file not found."

def update_score(question, filename, correct=True):
    """
    Update the score of the provided question based on user's answer.
    """
    with open(filename, 'r') as file:
        data = json.load(file)

    for qa_pair in data:
        if qa_pair['question'] == question:
            qa_pair['total_attempts'] += 1
            if correct:
                qa_pair['correct_attempts'] += 1
            break

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
