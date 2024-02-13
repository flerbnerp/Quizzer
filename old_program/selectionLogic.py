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

    # Filter out questions from the last batch
    qa_data = [qa for qa in qa_data if qa not in last_selected]

    # Calculate maximum correct attempts for weighting
    max_correct_attempts = max([qa.get("correct_attempts", 0) for qa in qa_data], default=0)
    
    # Return early if there's a problem with the data (e.g., all correct_attempts are 0)
    if max_correct_attempts == 0:
        max_correct_attempts = 0.0000001 # Avoid division by 0

    # Calculate scores for each question
    scored_qa = []
    for qa in qa_data:
        total_attempts = qa.get("total_attempts", 0)
        correct_attempts = qa.get("correct_attempts", 0)
        ratio = 0 if total_attempts == 0 else correct_attempts / total_attempts
        random_factor = random.randint(0, 25)
        score = 40 * ratio + 35 * (correct_attempts / max_correct_attempts) + random_factor
        scored_qa.append((score, qa))
    print(f"Total scored questions for {filepath}: {len(scored_qa)}")

    # Sort the scored questions by score
    scored_qa.sort(key=lambda x: x[0])

    # Handle tied scores
    threshold_score = scored_qa[num_questions_to_pick - 1][0] 
    tied_questions = [qa for score, qa in scored_qa if score == threshold_score]
    
    if len(tied_questions) > 1:
        random.shuffle(tied_questions)
        num_tied_to_pick = num_questions_to_pick - scored_qa.index((threshold_score, tied_questions[0]))
        selected_qas = scored_qa[:num_questions_to_pick - num_tied_to_pick] + [(threshold_score, qa) for qa in tied_questions[:num_tied_to_pick]]
    else:
        selected_qas = scored_qa[:num_questions_to_pick]
    print(f"Total tied questions for {filepath}: {len(tied_questions)}")

    # Update last_selected for the next call
    last_selected.clear()
    last_selected.extend([qa for _, qa in selected_qas])
    print(f"Final number of selected questions for {filepath}: {len(selected_qas)}")

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
        print(f"Selecting {num_questions_to_pick} questions from category: {category['qaCategory']}")

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

