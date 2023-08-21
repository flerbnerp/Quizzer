import os
import random
from initialize import initialize_education_directory
from initializeFilePath import construct_filepaths_directory
# from defineQA import setup_qa
from mainLoopDefines import get_md_content, update_score
from selectionLogic import get_weighted_question
from gui import guiMain

def launch_gui():
    guiMain.start_gui()

def main():
    # Initialize directories and config files
    initialize_education_directory()
    construct_filepaths_directory()
    # setup_qa()

    os.system('cls' if os.name == 'nt' else 'clear')
    choice = input("Enter 'start' to begin the question loop or 'gui' to launch GUI test module: ").lower()

    if choice == "gui":
        launch_gui()
        return
    
    # Main loop
    main_list = []  # A list to store the questions for the current batch

    while True:
        # If main_list is empty, repopulate it
        if not main_list:
            main_list = get_weighted_question()

        # Get a random question and its answer from the main list
        idx = random.randint(0, len(main_list) - 1)
        question, answer, filename = main_list.pop(idx)

        # 2. Prompt the user with the question
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Number of questions left in the main list: {len(main_list)}")
        user_input = input(f"\n{question}\nYour answer: ")

        # 3. Display the correct answer
        if answer.endswith(".md"):
            md_content = get_md_content(answer)
            print(f"\nCorrect Answer:\n{md_content}\n")
        else:
            print(f"\nCorrect Answer: {answer}\n")

        # 4. Prompt the user to continue
        while True:
            user_input = input("Question Correct? Enter Yes or No:").lower()

            if user_input == "yes":
                update_score(question, filename, correct=True)

                break
            elif user_input == "no":
                update_score(question, filename, correct=False)
                break
            elif user_input == "debug":
                break
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")

if __name__ == "__main__":
    main()
    
#Github instructions
# Run this first if you have made changes to the software on another system. Best to
# run this before you start working on the software on your system.
# git fetch origin
# git pull origin main

# Run these commands to push your changes to the repository
# git status
# git add .
# git commit -m "message"
# git push origin main