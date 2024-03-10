# This module holds functions relating to the updating of settings and configurations
# Currently we need to be able to update the quiz length, and subject weighting for quizzes
import json
def update_setting(key, value):
    # First load in settings.json
    with open("settings.json", "r") as f:
        settings = json.load(f)
    bad_value = False
    # Check functions for specific settings:
    if key == "quiz_length": # For now only quiz_length needs to be an integer, ie you can't have a fractional number of questions
        print("key is quiz_length")
        try:
            value = float(value)
            value = int(value)
        except ValueError:
            bad_value = True
    elif key == "vault_path":
        print("key is vault_path")
        if ("/" in value) or ("\\" in value):
            print("valid directory")
        else:
            print("invalid directory")
            bad_value = True
            return f"vault_path must be a directory path."
    elif key == "time_between_revisions":
        value = float(value)
    else:
        try:
            value = int(value)
        except ValueError:
            bad_value = True
    # Check if passed key is in the settings, if setting does not exist return an error
    if (key in settings) and bad_value == False:
        settings[key] = value
        with open("settings.json", "w") as f:
            json.dump(settings, f)
        return f"Updated setting:{key} to {settings[key]}"
    else:
        print("That setting does not exist in settings file")
        return "That setting does not exist in settings file"

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
    # Load all data into memory first:
    subject_set = get_subjects()
    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)
        # Setting check
        if settings.get("time_between_revisions") == None:
            settings["time_between_revisions"] = 1.10
            print("Initializing time between revisions setting key")
        else:
            print("time_between_revisions setting already exists")
        # Setting check    
        if settings.get("due_date_sensitivity") == None:
            print("due_date_sensitivity setting does not exist, initializing to 24")
            settings["due_date_sensitivity"] = 24
        else:
            print("due_date_sensitivity settings exists")
        # Setting check
        if settings.get("vault_path") == None:
            settings["vault_path"] = "/home/karibar/Documents/Education"   
        for i in subject_set:
            ##################################################
            # initialize subject weighting
            if settings.get(f"subject_{i}_weight") == None:
                print(f"key subject_{i}_weight missing, initializing key value to 1")
                settings[f"subject_{i}_weight"] = 1
            else:
                print(f"subject_{i}_weight exists in settings.json")
            ##################################################
            # initialize subject priority
            if settings.get(f"subject_{i}_priority") == None:
                print(f"key subject_{i}_weight missing, initializing key value to 1")
                settings[f"subject_{i}_priority"] = 1
            else:
                print(f"subject_{i}_priority exists in settings.json")
        
        with open("settings.json", "w") as f:
            json.dump(settings, f)
    except FileNotFoundError:
        print("settings.json is empty, initializing all keys")
        settings = {}
        # this setting controls the length of each quiz
        settings["quiz_length"] = 35
        settings["time_between_revisions"] = 1.10
        settings["due_date_sensitivity"] = 6
        settings["vault_path"] = "/home/karibar/Documents/Education"
        # this setting controls the weighting of questions for each quiz, default is an equal weighting across all subjects
        # User is encouraged to change this based on current classes being taken, but a minimum value of 1 is recommended for each subject
         # this block will be reused in the get_quiz() function to easily parse out the settings data
        for i in subject_set:
            settings[f"subject_{i}_weight"] = 1
            settings[f"subject_{i}_priority"] = 1
            
        # write settings data to questions.json file    
        with open("settings.json", "w") as f:
            json.dump(settings, f)