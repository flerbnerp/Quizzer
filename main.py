from initialize import initialize_education_directory
from initializeFilePath import construct_filepaths_directory
from defineQA import setup_qa
from mainLoopDefines import get_random_qa, get_md_content


def main():
    # Initialize directories and config files
    initialize_education_directory()
    construct_filepaths_directory()
    setup_qa()
    # Main loop
    while True:
        # 1. Get a random question and its answer
        question, answer = get_random_qa()

        # 2. Prompt the user with the question
        user_input = input(f"\n{question}\nYour answer: ")

        # 3. Display the correct answer
        if answer.endswith(".md"):
            md_content = get_md_content(answer)
            print(f"\nCorrect Answer:\n{md_content}\n")
        else:
            print(f"\nCorrect Answer: {answer}\n")

        # 4. Prompt the user to continue
        input("Enter any command to continue: ")

if __name__ == "__main__":
    main()