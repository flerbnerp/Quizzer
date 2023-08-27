import json
import random
import os
from mathQuestionGenerators import run_all_generators

QA_DIR = "qaJsonFiles"
CONFIG_DIR = "config"
CONFIG_FILE = "qaCategoriesConfig.json"

def select_questions_from_file(filepath, num_questions_to_pick=1):
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
        random_factor = random.random()
        try:
            score = 0.495 * ratio + 0.495 * (correct_attempts / max_correct_attempts) + 0.01 * random_factor
        except ZeroDivisionError:
            score = 0
        scored_qa.append((score, qa))

    # Sort the scored questions by score
    scored_qa.sort(key=lambda x: x[0])

    # Handle tied scores
    threshold_score = scored_qa[num_questions_to_pick - 1][0] 
    tied_questions = [qa for score, qa in scored_qa if score == threshold_score]
    
    if len(tied_questions) > 1:
        random.shuffle(tied_questions)
        num_tied_to_pick = num_questions_to_pick - scored_qa.index((threshold_score, tied_questions[0])) 
        # Use a list comprehension to maintain (score, qa) format for tied_questions
        selected_qas = scored_qa[:num_questions_to_pick - num_tied_to_pick] + [(threshold_score, qa) for qa in tied_questions[:num_tied_to_pick]]
    else:
        selected_qas = scored_qa[:num_questions_to_pick]

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
    print (len(main_list))
    return main_list  # Return the full list of question-answer pairs

