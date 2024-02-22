# This module holds functions relating to the updating of settings and configurations
# Currently we need to be able to update the quiz length, and subject weighting for quizzes
import json
def get_subjects():
    '''returns a set of subjects based on the subject key in questions.json'''
    with open("questions.json", "r") as f:
        data = json.load(f)
    subject_set = set([])
    for i in data:
        if "subject" in i and i["subject"] is not None:
            temp_list = i["subject"]
            for i in temp_list:
                subject_set.add(i)
    print(subject_set)
    print(type(subject_set))
                
                
def initialize_settings_json():
    '''creates settings.json if it doesn't exist'''
    try:
        with open("settings.json", "r") as f:
            print("settings.json exists")
    except:
        with open("settings.json", "x") as f:
            print("creating settings.json")
            
            
            
def initialize_settings_json_keys():
    '''Checks settings keys and initializes each key if it doesn't exist'''
    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)
    except:
        print("settings.json is empty, initializing all keys")
        settings = {}
        settings["quiz_length"] = 35
        with open("settings.json", "w") as f:
            json.dump(settings, f)
            
get_subjects()