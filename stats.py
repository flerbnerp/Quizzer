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
    

    
def print_stats():
    '''Collective function that prints all stats, which are based on individual functions'''
    print("Stats for Nerds!!!")
    with open("stats.json", "r") as f:
        stats_data = json.load(f)
    for key in stats_data:
        # Certain stats would be an average stat, in that case printing out the value of the key does not work. for example: average quiz_length would be calculated based on the average of list
        if key == "quiz_lengths": # One if statement for each specific stat that needs a calculation done to display:
            text = "Average quiz length taken"
            print(f"{text:<30}: {sum(stats_data[key]) / len(stats_data[key]):.2f}")
        else:
            print(f"{key:<30}: {stats_data[key]}")
    print()
    print_and_update_revision_streak_stats()
    