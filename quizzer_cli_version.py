##### Rebuilding Quizzer main interface in dummy_app:
import requests
import os
import urllib.parse
import base64
import json
import subprocess
##########################################################
# Launch and initialize api commands into string variables
command = "nohup uvicorn api:app --reload"
subprocess.Popen(command, shell=True)

root = "http://127.0.0.1:8000/"
command_pop_quiz = "populate_quiz"
command_get_stats = "stats"
command_initialize_quizzer = "initialize_quizzer"
command_completed_quiz = "completed_quiz"
command_update_score = "update_score"
##########################################################   
def begin_quiz():
    '''Quiz interface'''
    ## This function should not contain any processing of data, it should only make function calls to get information and display it.
    ## It is expected that this function will need to rewritten for every platform.
    data = requests.get(f"{root}{command_pop_quiz}")
    data = data.json()
    question_list = data["question_list"]
    returned_sorted_questions = data["sorted_questions"]
    os.system("clear")
    print("Welcome to Quizzer\nYou will be presented with a question, then prompted to either mark your answer right or wrong")
    print(f"This quiz contains {len(question_list)} questions out of {len(returned_sorted_questions)} available for review")
    user_input = input("press enter to continue or type exit to go back to the main menu")
    os.system("clear")
    
    # General process is to display the data from the question in index 0, once answered the question is removed from the list, pushing the second question into index 0,
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
            while valid_response == False:
                print("________________________________________________")
                user_input = input("Got it? Question Correct?")
                if user_input == "yes" or user_input == "y":
                    first_part = "http://127.0.0.1:8000/update_score/{status, file_name}?status=correct&file_name="
                    encoded_file_name = base64.b64encode(file_name.encode('utf-8')).decode('utf-8')
                    print(encoded_file_name)
                    query = first_part + encoded_file_name
                    response = requests.get(f"{query}")
                    print(response)
                    print(response.text)
                    valid_response = True
                    os.system("clear")
                elif user_input == "no" or user_input == "n":
                    first_part = "http://127.0.0.1:8000/update_score/{status, file_name}?status=incorrect&file_name="
                    encoded_file_name = base64.b64encode(file_name.encode('utf-8')).decode('utf-8')
                    query = first_part + encoded_file_name
                    response = requests.get(f"{query}")
                    print(response)
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
            data = requests.get(f"{root}{command_pop_quiz}")
            data = data.json()
            question_list = data["question_list"]
            returned_sorted_questions = data["sorted_questions"]
            print("You've completed a quiz!")
            print(f"The next quiz contains {len(question_list)} questions out of {len(returned_sorted_questions)} available for review")
            requests.get(f"{root}{command_completed_quiz}")
            user_input = input("Would you like to continue with another one?")
            if user_input == "yes":
                print("DID YOU SEE ME?")
                os.system("clear")
            elif user_input == "no":
                break
            else:
                print("Please enter a valid response")
        else:
            pass  
####################################################################
# If it takes an excessively long time to scan_directory, then we can simply add in the scan_directory as a menu option and update scan to write to file, for now it's only a few seconds to scan, If
# takes longer than a minute, then likely it would be beneficial to optimize.
# Currently its about 2000 notes and only a second to initialize. Given this it would require 10's of thousands of notes to become a problem
#################################################################################################################################################
# Initialize Quizzer using API
start_quizzer = requests.get(f"{root}{command_initialize_quizzer}")

#############################################################################
## Main Menu Interface:
error = False
while True:
    #### Options and other configuration stuff can be added here for the user.
    print("Welcome to Quizzer")
    print("You will be tested on a mixture of concepts and questions")
    print("Please select a menu option to begin")
    print("1: Begin quiz")
    print("2: Update quizzer")
    print("3: List Stats")
    print("4: Settings")
    print("5: Exit program")
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
        start_quizzer = requests.get(f"{root}{command_initialize_quizzer}")
        input("Press enter to continue")
    elif user_input == "3":
        os.system("clear")
        data = requests.get(f"{root}{command_get_stats}")
        data = data.json()
        for i in data:
            for i_line in data[i]:
                print(i_line)
        input("Press enter to continue")
    elif user_input == "4":
        os.system("clear")
        with open("settings.json", "r") as f:
            settings = json.load(f)
        for key, value in settings.items():
            string = f"{key} is set to:"
            underline = "_" * 50
            print(f"{string:<50} {value}\n{underline}")
        input("Press enter to continue")
    elif user_input == "5":
        break
    elif user_input == "debug":
        print("You've entered the secret admin debug area, no bugs here :D")
        input("Press enter to continue")
        
    else:
        error = True
    os.system("clear") # Since this is a CLI program, the interface is designed to be cleaned after every input, so the error variable is used to print the error message after this runs.  
