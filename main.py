from initialize import initialize_education_directory
from initializeFilePath import construct_filepaths_directory
from defineQA import setup_qa
from mainLoopDefines import get_md_content, update_score
from selectionLogic import get_weighted_question


def main():
    # Initialize directories and config files
    initialize_education_directory()
    construct_filepaths_directory()
    setup_qa()
    # Main loop
    while True:
        # 1. Get a random question and its answer
        question, answer = get_weighted_question()

        # 2. Prompt the user with the question
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
                update_score(question, correct=True)
                break
            elif user_input == "no":
                update_score(question, correct=False)
                break
            elif user_input == "debug":
                break
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")

if __name__ == "__main__":
    main()
    
#Github instructions
# git status
# git add .
# git commit -m "message"
# git push origin main
# git pull origin main
# git clone