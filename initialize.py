import os
import json
from datetime import datetime, timedelta
from settings import initialize_settings_json_keys, initialize_settings_json
from stats import initialize_stats_json
import ruamel.yaml
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
def initialize_question_metric_keys_if_they_dont_exist():
    '''
    takes a dictionary as an argument, then creates the key value pairs if they don't exist:
    "revision_streak" : 1
    "last_revised": datetime.now()
    "next_revision_due": datetime.now()
    returns a dictionary with the updated values, if they don't exist already
    '''
    with open("questions.json", "r") as f:
        questions = json.load(f)
    for dictionary in questions:
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
        if dictionary.get("question_media") == None or dictionary.get("question_media") == "":
            dictionary["question_media"] = "Error"
        if dictionary.get("answer_media") == None or dictionary.get("answer_media") == "":
            dictionary["answer_media"] = "Error"
        if dictionary.get("subject") == None:
            dictionary["subject"] = "no_subject"
        if dictionary.get("related") == None:
            dictionary["related"] = "no_relations"
        if dictionary.get("type") == None:
            dictionary["type"] = "no_type"
    with open("questions.json", "w") as f:
        json.dump(questions, f)
# def add_key_values():
# def parse_yaml_string(yaml_string):
#     print(yaml_string)
#     parsed_data = {}
#     list_value = []
#     parsing_multiline_value = False
#     key = "error"
#     for line in yaml_string.split("\n"):
#         # Attempting to build function methodically with if else statements
        
#         # My first question, is the line I'm looking at a property line or not?
#         if ":" in line:
#             property_line = True
#         elif ":" not in line:
#             property_line = False
#         else:
#             print("Something went wrong")
        
#         # if it's a property line, does it have a value attached? Grab the key, its a property
#         if property_line and len(list_value) != 0:
#             #Means we have finished iterating through a multiline property
#             parsed_data[key] = list_value
#             list_value = []
#         if property_line:
#             index = line.find(":")
#             key = line[:index]
#             split_line = line.strip().split(":")
#             if len(split_line) == 2:
#                 multiline = True
#                 split_line[1] = split_line[1].strip()
#                 parsed_data[key] = split_line[1]
#             # print(key)
#         elif not property_line: # We should have a key loaded in memory, but this is not the case
#             working_line = line.strip()
#             index = working_line.find("-") + 1
#             working_line = working_line[index:]
#             working_line = working_line.strip()
#             # print(f"working_line:{working_line}")
#             list_value.append(working_line)
            
#     # del parsed_data["error"]
#     return parsed_data

def parse_yaml():
    '''
    Does not take an argument, goes through the data.json list of file names and paths, and updates each object with any yaml that might exist
    '''
    start_delimiter, end_delimiter = "---\n", "---\n"
    data = []
    yaml = ruamel.yaml.YAML(typ='safe')
    with open("data.json", "r") as f:
        files = json.load(f)
    for file in files: # attempt to parse out yaml properties
        file_path = file["file_path"]
        if file_path.endswith(".md"):
            # open file contents
            with open(file_path, "r") as f:
                content = f.read() #contents of file now stored in content variable
            start_index = content.find(start_delimiter) + len(start_delimiter)
            end_index = content.find(end_delimiter, start_index)
            if start_index > -1 and end_index > -1:
                #Is yaml, attempt to parse

                yaml_properties = content[start_index:end_index].strip() # Strip out yaml properties
                print(yaml_properties)
                print(type(file))
                print(file)
                # print(f"THE YAML PROPERTIES ARE: \n{yaml_properties}\nITS TYPE IS {type(yaml_properties)}")
                if 'type: question' in yaml_properties:
                    note_dict = yaml.load(yaml_properties) # use yaml library to abstract the processing of properties
                    if type(file) == dict:
                        file.update(note_dict) # file should be a dictionary
                    data.append(file) #append our updated file object to our data list
                
                # We should now have our original file date name and path, plus whatever yaml exists in our file:
                else:
                    # Is not a question:
                    data.append(file) # append the file object to our data list
    print(len(data))
    with open("data.json", "w") as f:
        json.dump(data, f) # overwrite our data.json file with updated yaml.
    
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
                if is_media(file):
                    initialize_media_paths_json()
                    media_paths["file_paths"].append(os.path.join(root,file))
                else:
                    # Is not media
                    data = {}
                    file_name, extension = os.path.split(os.path.basename(file))
                    data["file_name"] = f"{file_name}.{extension}"
                    data["file_path"] = os.path.join(root,file)
                    concepts.append(data)
                # If file is not a known document or script file type, it is treated as media, missed checks do not effect integrity of data. Only contribute to storage size bloat

        with open("media_paths.json", "w") as f:
            json.dump(media_paths, f)
        with open("data.json", "w") as f:
            json.dump(concepts, f)    
    parse_yaml()
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
        if i.get("type") == "question":
            questions_list.append(i)
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
                    existing_question.update(new_question)
                    break
                # If there is no match, that means the question does not exist in our current questions.json
            if found == True:
                pass
            elif found == False:
                # For new entries, no scoring metrics will exist in that dictionary, we don't need to check if it's a question type since this function handles that already
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
    initialize_question_metric_keys_if_they_dont_exist()
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
