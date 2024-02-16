import json
with open("config.json", "r") as f:
    existing_data = json.load(f)
print(len(existing_data))