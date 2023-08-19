import json
import random

def get_random_qa():
    with open('qa.json', 'r') as file:
        qa_list = json.load(file)
    
    # Randomly select a QA pair
    random_qa = random.choice(qa_list)
    
    return random_qa['question'], random_qa['answer']

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
