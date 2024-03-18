import os
import yaml
import json
from datetime import datetime, timedelta
from settings import initialize_settings_json_keys, initialize_settings_json
from stats import initialize_stats_json
# use a dictionary
# Concept/question, subject, related
def is_media(file):
    '''Takes a string file_name.extension as an argument, returns True if the file is an image, else returns False'''
    if file.endswith(".md"):
        return False
    if file.endswith(".txt"):
        return False
    if file.endswith(".pdf"):
        return False
    if file.endswith(".doc"):
        return False
    if file.endswith(".docx"):
        return False
    if file.endswith(".js"):
        return False
    if file.endswith(".css"):
        return False
    if file.endswith(".mjs"):
        return False
    if file.endswith(".html"):
        return False
    if file.endswith(".woff"):
        return False
    if file.endswith(".ttf"):
        return False
    else:
        return True
def initialize_media_paths_json():
    '''Checks whether the media_paths.json exists, and creates media_paths.json if it doesn't exit'''
    try:
        with open("media_paths.json", "r") as f:
            media_paths = json.load(f)
    except FileNotFoundError:
        with open("media_paths.json", "w+") as f:
            json.dump({"file_paths": ["initialize_vale"]}, f)
        
    
def question_json_exists():
    """Checks if question.json exists. If not, create it.
    """
    try:
        with open("questions.json", "r"):
            pass
        print("questions.json exists")
    except:
        print("questions.json doesn't exist")
        print("creating questions.json")
        with open("questions.json", "x"):
            pass
def create_data_dot_json_if_doesnt_exist():
    '''checks if data.json exists or not, then creates data.json if does exist'''
    try:
        with open("data.json", "r"):
            pass
        print("data.json exists")
    except:
        print("data.json doesn't exist")
        print("creating data.json")
        with open("data.json", "x"):
            pass
def initialize_question_metric_keys_if_they_dont_exist(dictionary):
    '''
    takes a dictionary as an argument, then creates the key value pairs if they don't exist:
    "revision_streak" : 1
    "last_revised": datetime.now()
    "next_revision_due": datetime.now()
    returns a dictionary with the updated values, if they don't exist already
    '''
    if dictionary.get("revision_streak") == None:
        print("key 'revision_streak' does not exist, initializing key to 1")
        dictionary["revision_streak"] = 1
    if dictionary.get("last_revised") == None:
        print("key 'last_revised' does not exist, initializing key to datetime.now()")
        dictionary["last_revised"] = datetime.now()
        dictionary["last_revised"] = dictionary["last_revised"].strftime("%Y-%m-%d %H:%M:%S") # stringify for storage into .json
    if dictionary.get("next_revision_due") == None:
        print("key 'next_revision_due' does not exist, initializing key to datetime.now()")
        dictionary["next_revision_due"] = datetime.now()
        dictionary["next_revision_due"] = dictionary["next_revision_due"].strftime("%Y-%m-%d %H:%M:%S") # stringify for storage into .json
    if dictionary.get("question_text") == None:
        dictionary["question_text"] = "Error"
    if dictionary.get("answer_text") == None:
        dictionary["answer_text"] = "Error"
    if dictionary.get("question_media") == None:
        dictionary["question_media"] = "Error"
    if dictionary.get("answer_media") == None:
        dictionary["answer_media"] = "Error"
    if dictionary.get("subject") == None:
        dictionary["subject"] = "no_subject"
    if dictionary.get("related") == None:
        dictionary["related"] = "no_relations"
    if dictionary.get("type") == None:
        dictionary["type"] = "no_type"
    
    return dictionary
# def add_key_values():

def scan_directory(vault_path): # Returns a list(s) of dictionaries
    '''
    takes a list of file_paths as an argument
    scans the vault_path directory and stores the results in two seperate .json
    data.json contains a raw_list of all .md files
    media_paths.json contains the filepaths for all media in the provided directories
    '''
    create_data_dot_json_if_doesnt_exist() # Internal function check, make sure data.json actually exists before trying to write to it:
    for path in vault_path:
        concepts = []
        total_checks = 0
        media_paths = {"file_paths": []}
        for root, dirs, files in os.walk(path):
            # print(f"Scanning root: {root}")
            total_checks += 1
            for file in files:
                total_checks += 1
                # If a known text file, store in data.json (for now only .md)
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
                                #This check was added during the strip down phase
                                # convert datetime types to a json compatible type, otherwise scan fails with an error
                                if note_dict["due_date"] != None: 
                                    try:
                                        note_dict["due_date"] = note_dict["due_date"].strftime("%Y-%m-%d %H:%M:%S")
                                    except: #FIXME I have no idea what type of error this would produce?
                                        print("no idea?")
                                concepts.append(note_dict)
                            except:
                                pass
                # If file is not a known document or script file type, it is treated as media, missed checks do not effect integrity of data. Only contribute to storage size bloat
                elif is_media(file):
                    initialize_media_paths_json()
                    media_paths["file_paths"].append(os.path.join(root,file))
        with open("media_paths.json", "w") as f:
            json.dump(media_paths, f)
        with open("data.json", "w") as f:
            json.dump(concepts, f)    
        
    return concepts, total_checks
def extract_questions_from_raw_data():
    '''
    returns questions_list based on any question objects found in data.json
    checks the questions_list and intializes metrics for question objects
    '''
    question_json_exists()
    with open("data.json", "r") as f:
        existing_database = json.load(f)
    questions_list = []
    for i in existing_database:
        # print(f"question object: {i}")
        if i["type"] == "question":
            questions_list.append(i)
    for i in questions_list:
        initialize_question_metric_keys_if_they_dont_exist()
    return questions_list

def update_questions_json():
    '''
    checks new_questions against existing question objects in questions.json, then updates or adds the questions as necessary
    '''
    questions_list = extract_questions_from_raw_data() 
    ##################################################
    # Check to see if questions.json has data in it, if questions.json has no data, then we do a data dump of all new question objects: (could be abstracted) #FIXME
    try:
        with open("questions.json", "r") as f:
            questions_json = json.load(f)
            questions_json_has_data = True
    except:
        questions_json_has_data = False
        print("questions.json is empty")
        print("appending all questions from database to questions.json")
        print(f"There are {len(questions_list)} questions in questions.json")
        with open("questions.json", "w") as f:
            json.dump(questions_list, f)
    
    ##################################################
    # If questions.json has data we can initialize keys / scoring metric keys
    if questions_json_has_data == True:
    # At this step we have two lists of question type objects. Now we need to compare them and act accordingly
        for new_question in questions_list:
            found = False
            for existing_question in questions_json:
                # If we find a match, update the existing entry with the new entry, but only certain keys, this retains the scores while keeping updates working
                if new_question["file_name"] == existing_question["file_name"]:
                    found = True
                    existing_question = initialize_question_metric_keys_if_they_dont_exist(existing_question)
                    existing_question.update(new_question)
                    break
                # If there is no match, that means the question does not exist in our current questions.json
            if found == True:
                pass
            elif found == False:
                # For new entries, no scoring metrics will exist in that dictionary, we don't need to check if it's a question type since this function handles that already
                new_question = initialize_question_metric_keys_if_they_dont_exist(new_question)
                questions_json.append(new_question)
            else:
                print("oops something went wrong")
        # Now that we'd updated our questions.json we'll overwrite the old json file with the updated json file:
        
        total_questions_with_valid_keys = 0
        total_questions_with_invalid_keys = 0
        for i in questions_json:
            check = ""
            try:
                check = i["revision_streak"]
                total_questions_with_valid_keys += 1
            except:
                total_questions_with_invalid_keys
        print(f"There are {len(questions_json)} questions loaded into Quizzer.")
        print(f"There are {total_questions_with_valid_keys} questions with valid keys, and {total_questions_with_invalid_keys} with invalid keys.")
        
        with open("questions.json", "w")as f:
            json.dump(questions_json, f)    
            
def initialize_quizzer():
    # To initialize the program:
    # Step 1: load our settings.json
    timer_start = datetime.now()
    try: #FIXME not sure about the initialization for first time
        with open("settings.json", "r") as f:
            settings = json.load(f)
        vault_path = settings["vault_path"]
    except KeyError:
        vault_path = ["/home/karibar/Documents/Education"]
    # Step 2: Scan the provided directories, storing the data in json format (this is a raw dump so data is overwritten every time)
    scan_directory(vault_path)
    # Step 3: from the data.json data_dump extract the questions and modify the existing questions.json
    update_questions_json()
    # Step 4: Initialize settings file
    initialize_settings_json()
    initialize_settings_json_keys()
    # Step 5: Initialize stats.json file
    initialize_stats_json()
    timer_end = datetime.now()
    elapsed_time = timer_end - timer_start
    total_seconds = elapsed_time.total_seconds()
    minutes, seconds = divmod(total_seconds, 60)
    print(f"Success: initialization takes {int(minutes)} minutes and {int(seconds)} seconds.")
