import os
import json

def initialize_qa_categories():
    # Relative paths to the qaJsonFiles directory and config directory from the main directory
    qa_path = "qaJsonFiles"
    config_path = "config"

    # Check if the config file already exists
    config_file = os.path.join(config_path, "qaCategoriesConfig.json")
    
    # If the file exists, load its content to avoid overwriting the 'Number of questions to pick' field
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    new_data = []

    for file in os.listdir(qa_path):
        if file.endswith(".json"):
            # Check if this file already exists in the existing data
            existing_entry = next((item for item in existing_data if item["qaFileName"] == file), None)
            
            if existing_entry:
                # If it exists, append the existing entry to the new data
                new_data.append(existing_entry)
            else:
                # If it doesn't exist, create a new entry
                new_data.append({
                    "qaCategory": file.replace("qa", "").replace(".json", ""),
                    "qaFileName": file,
                    "qaFilePath": os.path.join(qa_path, file),
                    "Number of questions to pick": 1
                })

    # Save the new data to the config file
    with open(config_file, 'w') as f:
        json.dump(new_data, f, indent=4)

if __name__ == "__main__":
    initialize_qa_categories()
