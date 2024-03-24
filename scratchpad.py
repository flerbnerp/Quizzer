from urllib.parse import quote, unquote
from initialize import initialize_quizzer
import json
import re
import yaml
import requests
import os
from datetime import datetime, date
import math

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
    # for key, value in file["questions_answered"].items():
    #     if key == todays_date:
    




increment_questions_answered()







########################################################
# One time script to fix my boo boo error: update new question list with new format with old scoring
# Restore from backups
# with open("backups/questions.json", "r") as f:
#   old_questions = json.load(f)
# with open("questions.json", "r") as f:
#   new_questions = json.load(f)
# # for i in new_questions:
# #   print(i)
# matches = 0
# for old in old_questions:
#   old["file_name"] = "." + old["file_name"]
#   old["file_name"] = old["file_name"][:-4] + ".md"
#   for new in new_questions:
#     if old["file_name"] == new["file_name"]:
#       matches += 1
#       new["revision_streak"] = old["revision_streak"]
#       new["last_revised"] = old["last_revised"]
#       new["next_revision_due"] = old["next_revision_due"]
#       print(new)
#       break # since we found our match
# print(matches)
# with open("questions.json", "w") as f:
#   json.dump(new_questions, f)
# "revision_streaK"
# "last_revised"
# "next_revision_due"