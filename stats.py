import json
import math
from datetime import date
from quiz_functions import populate_question_list
def initialize_stats_json():
    try:
        with open("stats.json", "r") as f:
            print("stats.json already exists")
            print("-------------------------------------------------------")
    except:
        with open("stats.json", "x") as f:
            print("Creating stats.json")
            print("-------------------------------------------------------")
def increment_questions_answered():
    '''
    Embeds inside the update score function, increments the questions answered stat. Questions answered is stored by date, so the user can see a record of usage over time.
    '''
    todays_date = date.today()
    todays_date = str(todays_date)
    try:
        with open("stats.json", "r") as f:
            file = json.load(f)
        print("stats has data")
    except:
        print("stats has no data whatsoever")
        file = {}
    if file.get("questions_answered_by_date") == None: # First check, if the variable isn't there at all create the questioned answer dict stat
        print("questions_answered object does not exist, creating entry")
        file["questions_answered_by_date"] = {todays_date: 1}
    elif todays_date not in file["questions_answered_by_date"]: # Second check, if the user hasn't answered a questioned today then todays date will not be in the dictionary
        print("first question of the day, initializing new key: value for today's date")
        file["questions_answered_by_date"][todays_date] = 1
    else: # No check needed here, if the variable exists and the todays date exists as key we can safely access the key
        print("incrementing score for today")
        file["questions_answered_by_date"][todays_date] += 1
    file["total_questions_answered"] = sum(file["questions_answered_by_date"].values())
    with open("stats.json", "w") as f:
        json.dump(file, f)


def print_and_update_revision_streak_stats():
    # Load in data from json
    with open("questions.json", "r") as f:
        questions_data = json.load(f)
    with open("settings.json", "r") as f:
        settings = json.load(f)
    revision_stat_list = []
    revision_stat_set = set(revision_stat_list)
    for i in questions_data:
        revision_stat_list.append(i["revision_streak"])
        revision_stat_set.add(i["revision_streak"])
    # print("Revision Streak Stats:")
    revision_return_value = []
    revision_return_value.append("Revision Streak Stats:")
    average_questions_per_day = 0
    for i in revision_stat_set:
        count = revision_stat_list.count(i)
        average_questions_per_day += count * (1 / math.pow(settings["time_between_revisions"],i))
        # print(f"Questions with revision streak of {i} is {count}")
        revision_return_value.append(f"Questions with revision streak of {i} is {count}")   
    return revision_return_value, average_questions_per_day
        
        
def add_time():
    pass



def add_quiz_size():
    with open("settings.json", "r") as f:
        settings = json.load(f)
    quiz_length = settings["quiz_length"]
    with open("stats.json", "r") as f:
        stats_data = json.load(f)
    try:
        stats_data["quiz_lengths"] = list(stats_data["quiz_lengths"])
        stats_data["quiz_lengths"].append(quiz_length)
    except:
        stats_data["quiz_lengths"] = [quiz_length]
    with open("stats.json", "w") as f:
        json.dump(stats_data, f)
        
        
def completed_quiz():
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
    add_quiz_size()
    

    
def print_stats():
    '''Collective function that prints all stats, which are based on individual functions'''
    # print("Stats for Nerds!!!")
    stat_list = []
    stat_list.append("Stats for Nerds!!!")
    return_list, average_questions_per_day = print_and_update_revision_streak_stats()
    # with open("stats.json", "r") as f:
    #     stats_data = json.load(f)
    # for key in stats_data:
    #     # Certain stats would be an average stat, in that case printing out the value of the key does not work. for example: average quiz_length would be calculated based on the average of list
    #     if key == "quiz_lengths": # One if statement for each specific stat that needs a calculation done to display:
    #         text = "Average quiz length taken"
    #         # print(f"{text:<30}: {sum(stats_data[key]) / len(stats_data[key]):.2f}")
    #         stat_list.append(f"{text:<27}: {sum(stats_data[key]) / len(stats_data[key]):.2f}")
    #     else:
    #         # print(f"{key:<27}: {stats_data[key]}")
    #         stat_list.append(f"{key:<27}: {stats_data[key]}")
    # text = "Total Questions answered"
    # # print(f"{text:<30}: {sum(stats_data['quiz_lengths'])}")
    # stat_list.append(f"{text:<27}: {sum(stats_data['quiz_lengths'])}")
    # stat_list.append("--------------------------------")
    question_list, sorted_questions = populate_question_list()
    with open("questions.json", "r") as f:
        questions_raw_data = json.load(f)
    
    stat_list.append(f"Questions Stats:")
    stat_list.append(f"Total Questions in database: {len(questions_raw_data)}")
    stat_list.append(f"Questions up for review    : {len(sorted_questions)}")
    stat_list.append(f"Average Questions per day  : {average_questions_per_day:.3f}")
    stat_list.append("--------------------------------")
    stat_list = stat_list + return_list
    print("This is where text starts_________________________")
    for i in stat_list:
        print(i)
    return stat_list

