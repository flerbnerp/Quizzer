import json
import math
from datetime import date
from quiz_functions import populate_question_list
#FIXME
# One function per stat should exist
# each function should print the value of that stat to stats.jon
# API Calls should then only need to reference stats.json for statistics information.
#FIXME
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
    with open("stats.json", "r") as f:
        stats = json.load(f)
    # Get each level of revision that exists:
    revision_stat_list = []
    revision_stat_set = set(revision_stat_list)
    for i in questions_data:
        revision_stat_list.append(i["revision_streak"])
        revision_stat_set.add(i["revision_streak"])
    # Initialize variables
    average_questions_per_day = 0
    stats["revision_streak_stats"] = {}
    # loop through each unique level of revision and get the total questions with that level of revision
    for i in revision_stat_set:
        count = revision_stat_list.count(i)
        # In order to save memory, we gather this stat while were looping through each level of revision.
        average_questions_per_day += count * (1 / math.pow(settings["time_between_revisions"],i))
        stats["revision_streak_stats"][i] = count
    stats["average_questions_per_day"] = average_questions_per_day
    # Update stats.json with new information
    with open("stats.json", "w") as f:
        json.dump(stats, f)
    
def update_stat_total_questions_in_database():
    with open("questions.json", "r") as f:
        questions = json.load(f)
    with open("stats.json", "r") as f:
        stats = json.load(f)
    todays_date = date.today()
    todays_date = str(todays_date)
    total_questions_in_database = len(questions)
    metric = {todays_date: total_questions_in_database}
    if stats.get("total_questions_in_database") == None:
        print("initializing first intance of stat 'total_questions_in_database'")
        stats["total_questions_in_database"] = metric
    else:
        print("updating total_questions_in_database stat")
        stats["total_questions_in_database"][todays_date] = total_questions_in_database
    
    with open("stats.json", "w") as f:
        json.dump(stats, f)
    print(stats)
def update_stats():
    update_stat_total_questions_in_database()
    print_and_update_revision_streak_stats()

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

