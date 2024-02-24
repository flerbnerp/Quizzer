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
    return subject_set         
                
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
            
        if settings.get("time_between_revisions") == None:
            settings["time_between_revisions"] = 1.10
            print("Initializing time between revisions setting key")
        else:
            print("time_between_revisions setting already exists")
            
        if settings.get("due_date_sensitivity") == None:
            settings["due_date_sensitivity"] = 24
        else:
            print("due_date_sensitivity settings exists")    
        
        
        with open("settings.json", "w") as f:
            json.dump(settings, f)
    except:
        print("settings.json is empty, initializing all keys")
        settings = {}
        # this setting controls the length of each quiz
        settings["quiz_length"] = 35
        settings["time_between_revisions"] = 1.10
        # this setting controls the weighting of questions for each quiz, default is an equal weighting across all subjects
        # User is encouraged to change this based on current classes being taken, but a minimum value of 1 is recommended for each subject
        subject_set = get_subjects() # this block will be reused in the get_quiz() function to easily parse out the settings data
        for i in subject_set:
            settings[f"subject_{i}_weight"] = 1
            
        # write settings data to questions.json file    
        with open("settings.json", "w") as f:
            json.dump(settings, f)