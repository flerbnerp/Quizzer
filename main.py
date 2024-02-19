from initialize import initialize_or_update_json, initialize_master_question_list
from scoring_algorithm import generate_revision_schedule, update_score
from quiz_functions import populate_question_list
from stats import initialize_stats_json
import subprocess
import os
import random
import json
##########################################################   
def begin_quiz():
    question_list = populate_question_list() # Initialize question_list with questions
    os.system("clear")
    print("Welcome to Quizzer\nYou will be presented with a question, then prompted to either mark your answer right or wrong")
    user_input = input("press enter to continue or type exit to go back to the main menu")
    os.system("clear")
    while True:
        if len(question_list) > 0: # Check to see if the question_list is empty
            # user_input = input("\n\nEnter any key to continue: ")
            if user_input == "exit":
                os.system("clear")
                break
            # Quiz Interface
            # All question prompts will show the user the file name, the sub-type, and the subject being quizzed on:
            print(f"Questions remaining: {len(question_list)}")
            print(f"File name: {question_list[0]['file_name']}")
            try: # not all notes have a sub-type
                print(f"Type: {question_list[0]['sub-type']}")
            except:
                pass
            try: # quizzer crashed after presenting a note with no subject value, also this was a note of type: event which was not specificied to be pulled:
                print(f"Subject Matter: {question_list[0]['subject']}")
            except:
                pass
            try:
                print(f"Your revision streak on this question is {question_list[0]['revision_streak']}")
            except KeyError:
                pass
            try:
                print(f"This question was last revised on {question_list[0]['last_revised']}")
            except KeyError:
                pass
            try:
                print(f"Next revision is due: {question_list[0]['next_revision_due']}")
            except:
                pass
            ## Output will vary slightly based on the type value of the note:
            # For question notes:
            print(f"\nAnswer the following question:\n\n {question_list[0]['question_text']}")
            input("\nEnter any key to reveal the answer: ")
            print(f"\nRelated concepts: {question_list[0]['related']}")
            try:
                print(f"{question_list[0]['answer_text']}")
            except:
                print(f"no defined answer, check concept file")
                    
                    
            # Ask user whether they answered the question correct, then update score accordingly
            valid_response = False
            file_name = f"{question_list[0]['file_name']}"
            status = ""
            while valid_response == False:
                user_input = input("Got it? Question Correct?")
                if user_input == "yes" or user_input == "y":
                    status = "correct"
                    update_score(status, file_name)
                    valid_response = True
                    os.system("clear")
                elif user_input == "no" or user_input == "n":
                    status = "incorrect"
                    update_score(status, file_name)
                    valid_response = True
                    os.system("clear")
                elif user_input == "exit":
                    os.system("clear")
                    break
                elif user_input == "skip":
                    os.system("clear")
                    valid_response = True
                else:
                    print("enter either yes, y or no, n\n or type exit to quit")
            # Remove the item from the list.
            question_list.pop(0)



        elif len(question_list) <= 0: #Once the list is empty, go back and grab a new set of questions:
            os.system("clear")
            print("You've completed the first set of questions")
            user_input = input("Would you like to continue?")
            if user_input == "yes":
                question_list = populate_question_list()
            elif user_input == "no":
                break
            else:
                print("Please enter a valid response")
        else:
            pass
        
        
        
def initialize_quizzer(): # This function will contain all the initialization functions from various modules:
    # Scan provided file directory for all .md files and store data in config.json
    initialize_or_update_json() 
    initialize_master_question_list()
    # Initialize revision schedule for scoring algorithm
    try: #Don't generate the revision schedule if it already exists:
        with open("revision_schedule.json", "r") as f:
            pass
    except:
        generate_revision_schedule() # generates the revision schedule that will determine when notes will be served to the user
    
    # Initialize stats.json (if stats.json does not exist)
    initialize_stats_json()
    
####################################################################
if __name__ == "__main__":
    # If it takes an excessively long time to scan_directory, then we can simply add in the scan_directory as a menu option and update scan to write to file, for now it's only a few seconds to scan, If
    # takes longer than a minute, then likely it would be beneficial to optimize.
    # Currently its about 2000 notes and only a few seconds to initialize. Given this it would require 10's of thousands of notes to become a problem
    #################################################################################################################################################
    # Initialize variables
    vault_path = "/home/karibar/Documents/Education"
    error = False # for use if the user enters an invalid input
    #################################################################################################################################################
    ## Calling Initalization functions
    config_file_exists = False
    questions_file_exists = False
    
    try:
        with open("config.json", "r") as f:
            config_file_exists = True
    except:
        pass
    try:
        with open("questions.json", "r") as f:
            questions_file_exists = True
    except:
        pass
    if (config_file_exists == False) or (questions_file_exists == False):
        print("Missing files, long initialization in progress")
        initialize_quizzer()
        initialize_quizzer()
        initialize_quizzer()
    else:
        initialize_quizzer()
    #############################################################################
    ## Main Menu Interface:
    while True:
        #### Options and other configuration stuff can be added here for the user.
        print("Welcome to Quizzer")
        print("You will be tested on a mixture of concepts and questions")
        print("Please select a menu option to begin")
        print("1: Begin quiz")
        print("2: Update quizzer")
        print("3: List Stats")
        print("4: Exit program")
        if error == True:
            print("Enter a valid menu option:")
            error = False
        user_input = input("User: ")
        if user_input == "1":
            os.system("clear")
            begin_quiz()
        elif user_input == "2":
            os.system("clear")
            print("Updating Quizzer")
            initialize_quizzer()
            input("Press enter to continue")
        elif user_input == "3":
            os.system("clear")
            print("No stats module yet. . . Feature coming soon")
            input("Press enter to continue")
        elif user_input == "4":
            break
        else:
            error = True
        os.system("clear") # Since this is a CLI program, the interface is designed to be cleaned after every input, so the error variable is used to print the error message after this runs.  
    