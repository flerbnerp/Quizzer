import os
import json

CONFIG_FILE = "config.json"

def get_from_config(key):
    """Utility function to retrieve data from config file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
            return config.get(key)
    return None

def save_to_config(key, value):
    """Utility function to save data to config file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
    else:
        config = {}
    config[key] = value
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file)

def construct_filepaths_directory():
    # Retrieve the Education directory from the config
    education_dir = get_from_config('education_directory')
    if not education_dir:
        print("Education directory not found in config.")
        return
    
    # Construct the filepath directory by scanning the Education directory for all .md files
    filepath_directory = {}
    for root, dirs, files in os.walk(education_dir):
        for file in files:
            if file.endswith(".md"):
                filepath_directory[file] = os.path.join(root, file)
                
    # Save the filepath directory to the config
    save_to_config('filepaths', filepath_directory)
    print("Filepath directory constructed and saved to config.")

if __name__ == "__main__":
    construct_filepaths_directory()