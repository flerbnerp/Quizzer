# This will be based on the forgetting curve as first discovered by Ebbinghaus in 1880-1885
# Psuedo code for now
# scoring metrics
## {revision_streak: 1}
## {last_revised: YYYY-MM-DD-TTTT}
## {next_revision_due: YYYY-MM-DD-TTTT}
## If question correct
##     revision_streak += 1
##     last_revised = Current date and time
##     next_revision_due: = current date and time + revision schedule defines
## If question wrong
##     revision_streak = 1
##     last_revised = Current date and time
##     next_revision_due = current date and time + revision schedule defines
####################################################################################
## Proposed update to populate_quiz_list
## gather questions in a list (as done already)
## order list by next_revision_due in ascending order
## fill quiz_list starting from index[0] of the total_questions list
## this method would serve questions with revisions that are overdue, and then with revisions that have the shortest revision time remaining.
## questions with revisions, say 1 year from now, will be at the bottom of the list and thus won't be served to the user

def generate_revision_schedule():
    # Formula variables
    time_increment_between_revisions = 1.08 # 10% increase in time between revisions
    base_time = 60 * 24 # Initial time to second revision
    revision_number = 1
    file_write = ""
    x = 100
    while x > 0:
        file_write = file_write + (f"revision: {revision_number}, review again after, hours: {(base_time)/60:.3f}, days: {((base_time)/60)/24:.2f}\n")
        base_time = base_time * time_increment_between_revisions
        x -= 1
        revision_number += 1
    with open("revision_schedule.md", "w+") as f:
        f.write(file_write)
    
generate_revision_schedule()