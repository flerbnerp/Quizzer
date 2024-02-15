import json

with open("revision_schedule.json", "r") as f:
    schedule = json.load(f)
for entry in schedule: # look up how long until we need to review again in the revision schedule:
    if entry["revision_number"] == 2:
        time_till_next_review = entry["time_till_next_review"]
        print(time_till_next_review)
    else:
        pass # Not the correct entry, keep searching