import json
import random
import os
from mathQuestionGenerators import run_all_generators

QA_DIR = "qaJsonFiles"
CONFIG_DIR = "config"
CONFIG_FILE = "qaCategoriesConfig.json"

def select_questions_from_file(filepath, num_questions_to_pick=1, last_selected=[]):
    with open(filepath, 'r') as file:
        qa_data = json.load(file)

    # Calculate maximum correct attempts for weighting
    max_correct_attempts = max([qa.get("correct_attempts", 0) for qa in qa_data])

    # Calculate scores for each question
    scored_qa = []
    for qa in qa_data:
        total_attempts = qa.get("total_attempts", 0)
        correct_attempts = qa.get("correct_attempts", 0)
        ratio = 0 if total_attempts == 0 else correct_attempts / total_attempts
        random_factor = random.randint(0,100)
        try:
            score = 35 * ratio + 50 * (correct_attempts / max_correct_attempts) + 0.10 * random_factor
        except ZeroDivisionError:
            score = 0
        scored_qa.append((score, qa))

    # Sort the scored questions by score
    scored_qa.sort(key=lambda x: x[0])

    # Handle tied scores
    threshold_score = scored_qa[num_questions_to_pick - 1][0] 
    tied_questions = [qa for score, qa in scored_qa if score == threshold_score]
    
    if len(tied_questions) > 1:
        # Filter out questions from the last batch
        tied_questions = [qa for qa in tied_questions if qa not in last_selected]
        random.shuffle(tied_questions)
        num_tied_to_pick = num_questions_to_pick - scored_qa.index((threshold_score, tied_questions[0]))
        selected_qas = scored_qa[:num_questions_to_pick - num_tied_to_pick] + [(threshold_score, qa) for qa in tied_questions[:num_tied_to_pick]]
    else:
        selected_qas = scored_qa[:num_questions_to_pick]

    # Update last_selected for the next call
    last_selected.clear()
    last_selected.extend([qa for _, qa in selected_qas])

    return [(qa['question'], qa['answer']) for _, qa in selected_qas]

def get_weighted_question():
    # Run all generators
    run_all_generators()

    # Load the qaCategories configuration
    with open(os.path.join(CONFIG_DIR, CONFIG_FILE), 'r') as file:
        categories_config = json.load(file)

    main_list = []

    for category in categories_config:
        filepath = category["qaFilePath"]
        num_questions_to_pick = category["Number of questions to pick"]

        # Select the specified number of questions for the category
        selected_qas = select_questions_from_file(filepath, num_questions_to_pick)
        for q, a in selected_qas:
            main_list.append((q, a, filepath))
# Check length of main_list
    print (len(main_list))
# Check for duplicates in main_list
    unique_questions = set([q for q, _, _ in main_list])
    if len(unique_questions) != len(main_list):
        print(f"There are {len(main_list) - len(unique_questions)} duplicate questions.")
    else:
        print("No duplicate questions found.")
    return main_list  # Return the full list of question-answer pairs

