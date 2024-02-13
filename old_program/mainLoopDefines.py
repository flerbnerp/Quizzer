import json
import random
import os
from selectionLogic import get_weighted_question
from constants import QA_FILE

def get_md_content(file_name):
    """Retrieve the content of a markdown file based on its filename using config.json."""
    with open('config.json', 'r') as file:
        config = json.load(file)
        filepaths = config.get("filepaths", {})
        path_to_md = filepaths.get(file_name)
        
        if path_to_md:
            with open(path_to_md, 'r') as md_file:
                return md_file.read()
        else:
            return "Error: Markdown file not found."

def update_score(question, filename, correct=True):
    """
    Update the score of the provided question based on user's answer.
    """
    with open(filename, 'r') as file:
        data = json.load(file)

    for qa_pair in data:
        if qa_pair['question'] == question:
            qa_pair['total_attempts'] += 1
            if correct:
                qa_pair['correct_attempts'] += 1
            break

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        
def question_loop():
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