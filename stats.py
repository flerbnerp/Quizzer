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
    revision_stat_list = []
    revision_stat_set = set(revision_stat_list)
    for i in questions_data:
        revision_stat_list.append(i["revision_streak"])
        revision_stat_set.add(i["revision_streak"])
    print("Revision Streak Stats:")
    for i in revision_stat_set:
        count = revision_stat_list.count(i)
        print(f"Questions with revision streak of {i} is {count}")
        
        
        
def add_time():
    pass



def add_quiz_size(quiz_length):
    with open("stats.json", "r") as f:
        stats_data = json.load(f)
    if "quiz_lengths" in stats_data:
        stats_data["quiz_lengths"] = stats_data["quiz_lengths"].append(quiz_length)
    else:
        stats_data["quiz_lengths"] = [quiz_length]
    with open("stats.json", "w") as f:
        json.dump(stats_data, f)
        
        
        
def completed_quiz(quiz_length):
    try:
        with open("stats.json", "r") as f:
            stats_data = json.load(f)
        stats_data["number_of_quizzes_completed"] += 1
        with open("stats.json", "w") as f:
            json.dump(stats_data, f)
    except:
        initialze_dict = {"number_of_quizzes_completed": 1}
        with open("stats.json", "w") as f:
            json.dump(initialze_dict, f)
    add_time()
    add_quiz_size(quiz_length)