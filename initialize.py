import json
import os
import subprocess

CONFIG_FILE = "config.json"

def create_config():
    """Initialize a new configuration file."""
    # Check if the config file already exists
    if os.path.exists(CONFIG_FILE):
        print(f"{CONFIG_FILE} already exists.")
        return
    
    # Create an empty config file
    with open(CONFIG_FILE, 'w') as file:
        json.dump({}, file)
    print(f"{CONFIG_FILE} has been created.")

def read_config():
    """Read the configuration file and return its contents."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
        return config
    else:
        print(f"{CONFIG_FILE} does not exist.")
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

def get_from_config(key):
    """Utility function to retrieve data from config file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
            return config.get(key)
    return None

def find_education_directory():
    """Search for the 'Education/' directory within the /home directory and return its path."""
    
    command = ['find', '/home', '-type', 'd', '-iname', 'Education']
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    
    result = completed_process.stdout.strip().split('\n')
    
    if result and result[0]:
        # Assuming there might be multiple Education directories, take the first found one
        education_dir = result[0]
        
        # Save this directory to the config for future use
        save_to_config("education_directory", education_dir)
        
        return education_dir
    else:
        print("Education directory not found.")
        return None

def initialize_education_directory():
    # Create a config file
    create_config()
    # Read the created/available config
    config_content = read_config()
    if config_content is not None:
        print("")
    
    # Check if the directory is already in the config file
    existing_directory = get_from_config('education_directory')
    if existing_directory:
        print(f"Education directory found in config: {existing_directory}")
        
        # Validate if the existing_directory is still valid
        if os.path.exists(existing_directory) and os.path.isdir(existing_directory):
            print(f"Education directory is valid: {existing_directory}")
            return
        else:
            print(f"Education directory in config is no longer valid. Searching for a new directory...")

    # If not in the config or the existing directory is invalid, search for the Education directory
    education_dir = find_education_directory()
    if education_dir:
        print(f"New Education directory found: {education_dir}")
        save_to_config('education_directory', education_dir)
    else:
        print("Education directory not found.")


if __name__ == "__main__":
    initialize_education_directory()