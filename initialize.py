import os
import yaml
import json
import random
# use a dictionary
# Concept/question, subject, related
vault_path = "/home/karibar/Documents/Education"
def scan_directory(vault_path): # Returns a list(s) of dictionaries
    concepts = []
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root,file), "r", encoding="utf-8") as f:
                    content = f.read()  
                start_delimiter, end_delimiter = "---", "---\n"
                if start_delimiter and end_delimiter:
                    start_index = content.find(start_delimiter) + len(start_delimiter)
                    end_index = content.find(end_delimiter, start_index)
                    if start_index > -1 and end_index > -1:
                        yaml_properties = content[start_index:end_index].strip()
                        try:
                            note_dict = yaml.safe_load(yaml_properties)
                            filename, extension = os.path.splitext(os.path.basename(file))
                            full_filename = f"{filename}.{extension}"
                            note_dict["file_name"] = full_filename
                            note_dict["file_path"] = os.path.join(root,file)
                            concepts.append(note_dict)
                        except:
                            pass
    return concepts

def initialize_config_json():
    concepts = scan_directory(vault_path)
    main_dictionary_list = []
    with open("config.json", "w+") as f:
        for i in concepts:
            temp_dictionary = {"file_name": i["file_name"],"file_path": i["file_path"],"type": "", "subject": "", "related": ""}
            try:
                temp_dictionary["type"] = i["type"]
            except KeyError:
                print("??")
            try:
                temp_dictionary["subject"] = i["subject"]
            except KeyError:
                print("??")
            try:
                temp_dictionary["related"] = i["related"]
            except KeyError:
                print("??")
            if temp_dictionary["type"] == "question":
                try:
                    temp_dictionary["question_text"] = i["question_text"]
                except:
                    print("No question text")
                try:
                    temp_dictionary["answer_text"] = i["answer_text"]
                except:
                    print("no answer text")
            main_dictionary_list.append(temp_dictionary)
        json.dump(main_dictionary_list, f)
    # attempt_to_fill_data(concepts)   


# For testing, run this individual .py 
# concepts = scan_directory()
# print(concepts)
# initialize_config_json()
def populate_question_list():
    concepts = []
    questions = []
    with open("config.json", "r") as f:
        list_of_dictionaries = json.load(f)
    for i in list_of_dictionaries:
        if i["type"] == "Concept":
            concepts.append(i)
        if i["type"] == "question":
            questions.append(i)
    question_list = [] # empty the question list, prevents need to pass question_list into the function
    number_of_concepts = 18
    number_of_questions = 25
    while len(question_list) < number_of_concepts: # populates int(number_of_concepts) into the question list 
        rand = random.randint(0, len(concepts))
        question_list.append(concepts[rand])
    while len(question_list) < number_of_questions: # populates the difference betwene number_of_concepts and number_of_questions if 18 and 20, this populates 2 questions into the list
        rand = random.randint(0, len(questions))
        question_list.append(questions[rand])
    random.shuffle(question_list) # Shuffles the order of the list, without this, only concept notes will be presented then only questions.
    return question_list
    
populate_question_list()