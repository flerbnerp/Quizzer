from initialize import initialize_or_update_json
from scoring_algorithm import generate_revision_schedule
import subprocess
import os
import random
import json
def populate_question_list():
    concepts = []
    questions = []
    with open("config.json", "r") as f:
        list_of_dictionaries = json.load(f)
    for i in list_of_dictionaries:
        if i["type"] == "Concept":
            concepts.append(i)
        if i["type"] == "question":
            questions.append(i)
    question_list = [] # empty the question list, prevents need to pass question_list into the function
    number_of_concepts = 5
    number_of_questions = 25
    len_concepts = len(concepts) - 1
    len_questions = len(questions) - 1
    while len(question_list) < number_of_concepts: # populates int(number_of_concepts) into the question list 
        rand = random.randint(0, len_concepts)
        question_list.append(concepts[rand])
    while len(question_list) < number_of_questions: # populates the difference betwene number_of_concepts and number_of_questions if 18 and 20, this populates 2 questions into the list
        rand = random.randint(0, len_questions)
        question_list.append(questions[rand])
    random.shuffle(question_list) # Shuffles the order of the list, without this, only concept notes will be presented then only questions.
    return question_list
####################################################   
def begin_quiz():
    question_list = populate_question_list() # Initialize question_list with questions
    while True:
        if len(question_list) > 0: # Check to see if the question_list is empty
            user_input = input("\n\nEnter any key to continue: ")
            os.system("clear")
            if user_input == "exit":
                os.system("clear")
                break
            
            
            
            # Quiz Interface
            # All question prompts will show the user the file name, the sub-type, and the subject being quizzed on:
            print(f"File name: {question_list[0]['file_name']}")
            try: # not all notes have a sub-type
                print(f"Type: {question_list[0]['sub-type']}")
            except:
                pass
            try: # quizzer crashed after presenting a note with no subject value, also this was a note of type: event which was not specificied to be pulled:
                print(f"Subject Matter: {question_list[0]['subject']}")
            except:
                pass
            
            
            
            ## Output will vary slightly based on the type value of the note:
            # For concept notes:
            if f"{question_list[0]['type']}" == "Concept":
                print(f"\nPlease explain the following concept and what concepts might related to it: {question_list[0]['file_name']}")
                input(f"Enter any key to reveal related concepts: ")
                print(f"Related Concepts: {question_list[0]['related']}")
            # For question notes:
            if f"{question_list[0]['type']}" == "question":
                print(f"\nAnswer the following question:\n\n {question_list[0]['question_text']}")
                input("\nEnter any key to reveal the answer: ")
                print(f"\nRelated concepts: {question_list[0]['related']}")
                try:
                    print(f"{question_list[0]['answer_text']}")
                except:
                    print(f"no defined answer, check concept file")
            # Remove the item from the list.
            question_list.pop(0)



        elif len(question_list) <= 0: #Once the list is empty, go back and grab a new set of questions:
            print("Getting new set of questions. . .")
            question_list = populate_question_list()
        else:
            pass
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
    initialize_or_update_json() # Scan Obsidian vault for questions, generates a list of dictionaries
    generate_revision_schedule() # generates the revision schedule that will determine when notes will be served to the user
    
    
    
    #############################################################################
    ## Main Menu Interface:
    while True:
        #### Options and other configuration stuff can be added here for the user.
        print("Welcome to Quizzer")
        print("You will be tested on a mixture of concepts and questions")
        print("Please select a menu option to begin")
        print("1: begin quiz")
        print("2: exit program")
        if error == True:
            print("Enter a valid menu option:")
            error = False
        user_input = input("User: ")
        if user_input == "1":
            os.system("clear")
            begin_quiz()
        elif user_input == "2":
            break
        else:
            error = True
        os.system("clear") # Since this is a CLI program, the interface is designed to be cleaned after every input, so the error variable is used to print the error message after this runs.  
    