from initialize import scan_directory
import subprocess
import os
import random
def populate_question_list(concepts, questions):
    question_list = [] # empty the question list, prevents need to pass question_list into the function
    number_of_concepts = 18
    number_of_questions = 25
    while len(question_list) < number_of_concepts: # populates int(concepts) into the question list 
        rand = random.randint(0, len(concepts))
        question_list.append(concepts[rand])
    while len(question_list) < number_of_questions: # populates the difference betwene num_concepts and num_questions if 18 and 20, this populates 2 questions into the list
        rand = random.randint(0, len(questions))
        question_list.append(questions[rand])
    random.shuffle(question_list)
    return question_list   
def begin_quiz(concepts, questions):
    question_list = []
    while True:
        if len(question_list) > 0:
            user_input = input("\n\nEnter any key to continue: ")
            os.system("clear")
            if user_input == "exit":
                os.system("clear")
                break
            # Quiz Interface
            print(f"File name: {question_list[0]['file_name']}")
            try:
                print(f"Type: {question_list[0]['sub-type']}")
            except:
                pass
            print(f"Subject Matter: {question_list[0]['subject']}")
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
            question_list = populate_question_list(concepts, questions)
        else:
            pass

if __name__ == "__main__":
    # If it takes an excessively long time to scan_directory, then we can simply add in the scan_directory as a menu option and update scan to write to file, for now it's only a few seconds to scan, If
    # takes longer than a minute, then likely it would be beneficial to optimize.
    # Currently its about 2000 notes and only a few seconds to initialize. Given this it would require 10's of thousands of notes to become a problem
    concepts, questions = scan_directory()
    error = False
    while True:
        print("Welcome to Quizzer")
        print(f"There are {len(concepts)} concept notes and {len(questions)} question notes")
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
            begin_quiz(concepts, questions)
        elif user_input == "2":
            break
        else:
            error = True
        os.system("clear")  
        
# Planned changes:
## add in historical_person notes to quizzer, this list will quiz on birth and death dates
### Who the person was and why they were important:

## add in config options
### First option to tell quizzer, how many of each type of question to present in each quiz

## Scoring methodology
### get filename.md
### add scoring metrics
### add above to json file for permanent storage
### Scan will check whether filename.md in concepts, questions, people, 
### already exists in the scoreboard.json. If not, add in new json object to represent the file:
### every object will contain the yaml properties, subject, related, question_text, answer_text, 
#### Scores should never be overwritten, but json objects should update based when 
#### files in obsidian changes

## Update quiz function to take advantage of scoring metrics
### this will require quizzer to pull questions from the .json file instead of from a prescanned list.
### Updates quiz function will have an algorithm to determine how to populate the quiz based on current scoring metrics:

## add in config option: questions by subject
### Only effects the question type

# Change Log
## 