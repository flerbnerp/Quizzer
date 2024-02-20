import json
def initialize_stats_json():
    try:
        with open("stats.json", "r") as f:
            print("stats.json already exists")
            print("-------------------------------------------------------")
    except:
        with open("stats.json", "x") as f:
            print("Creating stats.json")
            print("-------------------------------------------------------")

def print_and_update_revision_streak_stats():
    # Load in data from json
    with open("questions.json", "r") as f:
        questions_data = json.load(f)
    with open("revision_schedule.json", "r"):
        revision_schedule = json.load(f)
    # generate variables based on range of values in revision streak
    