import os
import yaml
import json
from datetime import datetime, timedelta
# use a dictionary
# Concept/question, subject, related
vault_path = "/home/karibar/Documents/Education"
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
def create_config_dot_json_if_doesnt_exist():
    try:
        with open("config.json", "r"):
            pass
        print("config.json exists")
    except:
        print("config.json doesn't exist")
        print("creating config.json")
        with open("config.json", "x"):
            pass
def initialize_score_metric_keys_if_they_dont_exist(dictionary):    
    check_variable = ""
    try:
        check_variable = dictionary["revision_streak"]
    except KeyError:
        # print("Key does not exist, Initializing Key") # Initialiaze key, since it doesn't exist
        dictionary["revision_streak"] = 1
    try: 
        check_variable = dictionary["last_revised"]
    except KeyError:
        # print("Key does not exist, Initializing Key") # Initialiaze key, since it doesn't exist
        dictionary["last_revised"] = datetime.now()
        dictionary["last_revised"] = dictionary["last_revised"].strftime("%Y-%m-%d %H:%M:%S")             
    try:
        check_variable = dictionary["next_revision_due"]
    except KeyError:
        # print("Key does not exist, Initializing Key") # Initialiaze key, since it doesn't exist
        dictionary["next_revision_due"] = datetime.now() + timedelta(hours=24)
        # Convert value to a string, so it can be written to config.json
        dictionary["next_revision_due"] = dictionary["next_revision_due"].strftime("%Y-%m-%d %H:%M:%S")
    return dictionary
def scan_directory(vault_path): # Returns a list(s) of dictionaries
    concepts = []
    total_checks = 0
    for root, dirs, files in os.walk(vault_path):
        total_checks += 1
        for file in files:
            total_checks += 1
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
    return concepts, total_checks      
def initialize_or_update_json():
### Scan Vault and produce new data to append based on the data in the vault:
    create_config_dot_json_if_doesnt_exist()
    concepts, total_checks = scan_directory(vault_path)
    new_data = []
    # counters for debugging purposes:
    dicts_to_be_added = []
    total_file_matches = 0
    added_to_existing_data = 0
    
    
    # this loop ensures all keys exist in each dictionary object, prevents keyerrors, most users will likely not have any valid properties attached already:
    for i in concepts:
            total_checks += 1
            temp_dictionary = {"file_name": i["file_name"],"file_path": i["file_path"],"type": "", "subject": "", "related": ""}
            try:
                temp_dictionary["type"] = i["type"]
            except KeyError:
                pass
            try:
                temp_dictionary["subject"] = i["subject"]
            except KeyError:
                pass
            try:
                temp_dictionary["related"] = i["related"]
            except KeyError:
                pass
            if temp_dictionary["type"] == "question":
                try:
                    temp_dictionary["question_text"] = i["question_text"]
                except KeyError:
                    pass
                try:
                    temp_dictionary["answer_text"] = i["answer_text"]
                except KeyError:
                    pass  
            new_data.append(temp_dictionary)
### append or update existing_data with new_data if config.json has existing data in it
    try:
        with open("config.json", "r") as f:
            existing_data = (json.load(f))

        # Second Loop append any newly scanned data that doesn't exist in existing_data
        # Since we can't check if data is new or old based on the length of the lists, we can manually check each with a Boolean
        for updated_dict in new_data: # check if new data exists in old data, if the file is not in old data it should be appended since there is nothing to update:
            found = False
            total_checks += 1
            for existing_dict in existing_data:
                total_checks += 1
                if updated_dict["file_name"] == existing_dict["file_name"]:
                    found = True
                    existing_dict.update(updated_dict)
                    break
            if found == True:
                total_file_matches += 1
            elif found == False:
                existing_data.append(updated_dict)
                added_to_existing_data += 1
            else:
                print("This went wrong?")
            
            # We should now have an updated existing_data object to overwrite our config.json with
        with open("config.json", "w") as f: # Write the updated list of dictionaries to config.json
            json.dump(existing_data, f)
### Quality checks
        print(f"Total items not found in existing items is: {len(dicts_to_be_added)}")
        for i in dicts_to_be_added:
            print(f"{i['question_text']}\n")
        print(f"Added a total of {added_to_existing_data} new entries to config.json")
        print(f"There are {len(new_data)} items in the most recent scan")
        print(f"Total file matches is: {total_file_matches} compared to {len(existing_data)-added_to_existing_data} pre-existing files in Vault")
        print(f"total operations to complete scan is: {total_checks:,}")
        print(f"-------------------------------------------------------")
    except:
        with open("config.json", "w") as f:
            json.dump(new_data, f)
    # If the file does not exist, create config.json and dump new_data into it:
    return total_checks

def initialize_master_question_list():
    question_json_exists()
    with open("config.json", "r") as f:
        existing_database = json.load(f)
    # Parse out the question objects from our config.json file
    questions_in_existing_database = []
    for i in existing_database:
            if i['type'] == "question":
                questions_in_existing_database.append(i)  
                
                
                
    # Check to see if questions.json has data in it:
    try:
        with open("questions.json", "r") as f:
            questions_json = json.load(f)
            questions_json_has_data = True
    except:
        questions_json_has_data = False
        print("questions.json is empty")
        print("appending all questions from database to questions.json")
        print(f"There are {len(questions_in_existing_database)} questions in questions.json")
        with open("questions.json", "w") as f:
            json.dump(questions_in_existing_database, f)
    
    # If questions.json has data we can initialize keys / scoring metric keys
    if questions_json_has_data == True:
    # At this step we have two lists of question type objects. Now we need to compare them and act accordingly
        for new_question in questions_in_existing_database:
            found = False
            for existing_question in questions_json:
                # If we find a match, update the existing entry with the new entry, but only certain keys, this retains the scores while keeping updates working
                if new_question["file_name"] == existing_question["file_name"]:
                    found = True
                    existing_question = initialize_score_metric_keys_if_they_dont_exist(existing_question)
                    existing_question.update(new_question)
                    break
                # If there is no match, that means the question does not exist in our current questions.json
            if found == True:
                pass
            elif found == False:
                # For new entries, no scoring metrics will exist in that dictionary, we don't need to check if it's a question type since this function handles that already
                new_question = initialize_score_metric_keys_if_they_dont_exist(new_question)
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
            
    # If file is empty get all question objects and append them to the file, job done.

    
    # Debug values against expected values:
    # total_questions = 0
    # for i in questions_in_existing_database:
    #     if i['type'] == "question":
    #         total_questions += 1
    # is_working = total_questions == len(questions_in_existing_database)
    # print(f"There are {len(questions_in_existing_database)} dict objects in questions.json")
    # print(f"There are {total_questions} question type dict objects in questions.json")
    # print(f"The question list initialization is working as expected: {is_working}")