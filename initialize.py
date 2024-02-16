import os
import yaml
import json
from datetime import datetime, timedelta
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
def initialize_or_update_json():
### Scan Vault and produce new data to append based on the data in the vault:
    concepts = scan_directory(vault_path)
    new_data = []
    for i in concepts:
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
                except:
                    pass
                try:
                    temp_dictionary["answer_text"] = i["answer_text"]
                except:
                    pass                
            new_data.append(temp_dictionary)
### append or update existing_data with new_data if config.json exists:
    counter = 0
    try: # if the file is empty then we move to the except block:
        with open("config.json", "r") as f:
            existing_data = (json.load(f))
        # Update existing_data with newly scanned data:
        for existing_dict in existing_data:
            check_variable = ""
            if existing_dict["type"] == "question":
                try:
                    check_variable = existing_dict["revision_streak"]
                except KeyError:
                    print("Key does not exist, Initializing Key") # Initialiaze key, since it doesn't exist
                    existing_dict["revision_streak"] = 1
                try: 
                    check_variable = existing_dict["last_revised"]
                except KeyError:
                    print("Key does not exist, Initializing Key") # Initialiaze key, since it doesn't exist
                    existing_dict["last_revised"] = datetime.now()
                    existing_dict["last_revised"] = existing_dict["last_revised"].strftime("%Y-%m-%d %H:%M:%S")             
                try:
                    check_variable = existing_dict["next_revision_due"]
                except KeyError:
                    print("Key does not exist, Initializing Key") # Initialiaze key, since it doesn't exist
                    existing_dict["next_revision_due"] = datetime.now() + timedelta(hours=24)
                    # Convert value to a string, so it can be written to config.json
                    existing_dict["next_revision_due"] = existing_dict["next_revision_due"].strftime("%Y-%m-%d %H:%M:%S")     
            for updated_dict in new_data:
                if existing_dict["file_name"] == updated_dict["file_name"]: #If the updated_dict we are iterating over is found, update the existing entry
                    existing_dict.update(updated_dict)
                    counter += 1
                    break
                
        # counters for debugging purposes:
        dicts_to_be_added = []
        total_file_matches = 0
        total_checks = 0
        added_to_existing_data = 0
        # Second Loop append any newly scanned data that doesn't exist in existing_data
        # Since we can't check if data is new or old based on the length of the lists, we can manually check each with a Boolean
        for updated_dict in new_data:
            found = False
            for existing_dict in existing_data:
                total_checks += 1
                if updated_dict["file_name"] == existing_dict["file_name"]:
                    found = True
            if found == True:
                total_file_matches += 1
            elif found == False:
                dicts_to_be_added.append(updated_dict)
        try: # if there is no new data to be added the following throws an error. I threw it in a try except block, because I don't care about that error:
            for i in dicts_to_be_added:
                existing_data.append(i)
                added_to_existing_data += 1
        except:
            pass
        with open("config.json", "w") as f: # Write the updated list of dictionaries to config.json
            json.dump(existing_data, f)
### Quality checks
        print(f"Total items not found in existing items is: {len(dicts_to_be_added)}")
        print(f"Added a total of {added_to_existing_data} new entries to config.json")
        print(f"There are {len(new_data)} items in the most recent scan")
        print(f"Total file matches is: {total_file_matches} compared to {len(existing_data)-added_to_existing_data} pre-existing files in Vault")
        print(f"total operations to complete scan is: {total_checks:,}")
        print(f"-------------------------------------------------------")
    # If the file exists, create config.json and dump new_data into it:
    except:
        for existing_dict in new_data:
            check_variable = ""
            if existing_dict["type"] == "question":
                try:
                    check_variable = existing_dict["revision_streak"]
                except KeyError:
                    print("Key does not exist, Initializing Key") # Initialiaze key, since it doesn't exist
                    existing_dict["revision_streak"] = 1
                try: 
                    check_variable = existing_dict["last_revised"]
                except KeyError:
                    print("Key does not exist, Initializing Key") # Initialiaze key, since it doesn't exist
                    existing_dict["last_revised"] = datetime.now()
                    existing_dict["last_revised"] = existing_dict["last_revised"].strftime("%Y-%m-%d %H:%M:%S")             
                try:
                    check_variable = existing_dict["next_revision_due"]
                except KeyError:
                    print("Key does not exist, Initializing Key") # Initialiaze key, since it doesn't exist
                    existing_dict["next_revision_due"] = datetime.now() + timedelta(hours=24)
                    # Convert value to a string, so it can be written to config.json
                    existing_dict["next_revision_due"] = existing_dict["next_revision_due"].strftime("%Y-%m-%d %H:%M:%S")        
        print("No File Exists, Initializing config.json")
        with open("config.json", "w+") as f:
            json.dump(new_data, f)

                
# def initialize_config_json():
#     concepts = scan_directory(vault_path)
#     main_dictionary_list = []
#     try:
#         with open("config.json", "r") as f:
#             existing_data = (json.load(f))
#             print(type(existing_data))
#     except:
#         print("file is empty")
#     with open("config.json", "w+") as f:
#         for i in concepts:
#             temp_dictionary = {"file_name": i["file_name"],"file_path": i["file_path"],"type": "", "subject": "", "related": ""}
#             try:
#                 temp_dictionary["type"] = i["type"]
#             except KeyError:
#                 pass
#             try:
#                 temp_dictionary["subject"] = i["subject"]
#             except KeyError:
#                 pass
#             try:
#                 temp_dictionary["related"] = i["related"]
#             except KeyError:
#                 pass
#             if temp_dictionary["type"] == "question":
#                 try:
#                     temp_dictionary["question_text"] = i["question_text"]
#                 except:
#                     pass
#                 try:
#                     temp_dictionary["answer_text"] = i["answer_text"]
#                 except:
#                     pass                
#             main_dictionary_list.append(temp_dictionary)
#         json.dump(main_dictionary_list, f)
    # new_data = main_dictionary_list
    # return new_data

        
    # attempt_to_fill_data(concepts)   


# For testing, run this individual .py 
# concepts = scan_directory()
# print(concepts)
# initialize_or_update_json()
# initialize_or_update_json()
