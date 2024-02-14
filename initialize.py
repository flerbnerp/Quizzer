import os
import yaml
import json
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
            main_dictionary_list.append(temp_dictionary)
        json.dump(main_dictionary_list, f)
    # attempt_to_fill_data(concepts)   


# For testing, run this individual .py 
# concepts = scan_directory()
# print(concepts)
# initialize_config_json()
initialize_config_json()