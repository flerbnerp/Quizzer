import json
from datetime import datetime, timedelta
# This will be based on the forgetting curve as first discovered by Ebbinghaus in 1880-1885
####################################################################################
## Proposed update to populate_quiz_list
## gather questions in a list (as done already)
## order list by next_revision_due in ascending order
## fill quiz_list starting from index[0] of the total_questions list
## this method would serve questions with revisions that are overdue, and then with revisions that have the shortest revision time remaining.
## questions with revisions, say 1 year from now, will be at the bottom of the list and thus won't be served to the user

def generate_revision_schedule():
    # Formula variables
    with open("settings.json", "r") as f:
        settings = json.load(f)
    time_increment_between_revisions = settings["time_between_revisions"] # 10% increase in time between revisions
    base_time = 24 # Initial time to second revision
    revision_number = 1
    file_write = ""
    x = 500
    revision_schedule = []
    revision_key_value = {}
    while x > 0:
        revision_key_value = {"revision_number": revision_number, "time_till_next_review": base_time}
        revision_schedule.append(revision_key_value)
        base_time = base_time * time_increment_between_revisions
        x -= 1
        revision_number += 1
    with open("revision_schedule.json", "w+") as f:
        json.dump(revision_schedule, f)
    
def update_score(status, file_name):
    with open("settings.json", "r") as f:
        settings = json.load(f)
    check_variable = ""
    bad_matches = 0
    # load config.json into memory, I get the feeling this is poor memory management, but it's only 1000 operations.
    with open("questions.json", "r") as f:
        existing_data = (json.load(f))
    for dictionary in existing_data:
        if dictionary["file_name"] == file_name:
            # Alternatively this could have been a seperate function for initializing, both work:
            ############# We Have Three Values to Update ########################################
            try: ###############################################
                check_variable = dictionary["revision_streak"]
                print(f"Revision streak was {check_variable}, streak is now {check_variable + 1}")
                if status == "correct":
                    dictionary["revision_streak"] = dictionary["revision_streak"] + 1
                elif status == "incorrect":
                    dictionary["revision_streak"] = 1
            except KeyError:
                print("Key does not exist, Initializing Key") # Initialiaze key, since it doesn't exist
                dictionary["revision_streak"] = 1
            try: ###############################################
                check_variable = dictionary["last_revised"]
                print(f"This question was last revised on {check_variable}")
                # Convert string json value back to a <class 'datetime.datetime'> type variable so it can be worked with:
                dictionary["last_revised"] = datetime.strptime(dictionary["last_revised"], "%Y-%m-%d %H:%M:%S")
                dictionary["last_revised"] = datetime.now()
                # Convert value back to a string so it can be written back to the json file
                dictionary["last_revised"] = dictionary["last_revised"].strftime("%Y-%m-%d %H:%M:%S")
            except KeyError:
                print("Key does not exist, Initializing Key") # Initialiaze key, since it doesn't exist
                dictionary["last_revised"] = datetime.now()
                dictionary["last_revised"] = dictionary["last_revised"].strftime("%Y-%m-%d %H:%M:%S")
            try: ###############################################
                
                # Convert string json value back to a <class 'datetime.datetime'> type variable so it can be worked with:
                dictionary["next_revision_due"] = datetime.strptime(dictionary["next_revision_due"], "%Y-%m-%d %H:%M:%S")
                
                # Next revision due is based on the schedule that was outputted from the generate_revision_schedule() function:
                # If question was correct, update according to schedule, otherwise set next due date according to sensitivity settings so question is immediately available again for review regardless of what the user enters
                if status == "correct":
                    with open("revision_schedule.json", "r") as f:
                        schedule = json.load(f)
                    for entry in schedule: # look up how long until we need to review again in the revision schedule:
                        if entry["revision_number"] == dictionary["revision_streak"]:
                            time_till_next_review = entry["time_till_next_review"]
                        else:
                            pass # Not the correct entry, keep searching
                    dictionary["next_revision_due"] = datetime.now() + timedelta(hours=time_till_next_review)
                else: # if not correct then incorrect, function should error out if status is not fed into properly:
                    if settings["due_date_sensitivity"] >= 24: # If the user sets a very high value for sensitivity, ensure that the value is no greater than the revision schedules base time:
                        settings["due_date_sensitivity"] = 24
                    dictionary["next_revision_due"] = datetime.now() + timedelta(hours=settings["due_date_sensitivity"])
                # Convert value back to a string so it can be written back to the json file
                dictionary["next_revision_due"] = dictionary["next_revision_due"].strftime("%Y-%m-%d %H:%M:%S")
                check_variable = dictionary["next_revision_due"]
                print(f"The next revision is due on {check_variable}")
            except KeyError:
                print("Key does not exist, Initializing Key") # Initialiaze key, since it doesn't exist
                dictionary["next_revision_due"] = datetime.now()
                # Convert value to a string, so it can be written to config.json
                dictionary["next_revision_due"] = dictionary["next_revision_due"].strftime("%Y-%m-%d %H:%M:%S")     
        else:
            bad_matches += 1
    with open("questions.json", "w") as f:
        json.dump(existing_data, f)
    # Debug Statements:
    # print(bad_matches)
    # print(file_name)
    # print(type(file_name))
    # input("Debug, press enter to continue:")
