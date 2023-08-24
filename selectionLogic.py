import json
import random
import os
from mathQuestionGenerators import run_all_generators

QA_DIR = "qaJsonFiles"
CONFIG_DIR = "config"
CONFIG_FILE = "qaCategoriesConfig.json"
# Configurable selection logic
lowestRatio = 50 # Lowest ratio of correct to total attempts, algorithm will select this many questions from the lowest ratio scoring QA pairs.
lowestCorrectAttempts = 49 # Lowest number of correct attempts, algorithm will select this many questions from the lowest correct attempts scoring QA pairs.
randomPick = 1 # Randomly select this many questions from the QA pairs.

def select_questions_from_file(filepath, num_questions_to_pick=1):
    with open(filepath, 'r') as file:
        qa_data = json.load(file)

    indexed_ratios = []
    indexed_correct_attempts = []
    for index, qa in enumerate(qa_data):
        total_attempts = qa.get("total_attempts", 0)
        correct_attempts = qa.get("correct_attempts", 0)
        ratio = 0 if total_attempts == 0 else correct_attempts / total_attempts
        indexed_ratios.append((ratio, index))
        indexed_correct_attempts.append((correct_attempts, index))
    indexed_ratios.sort(key=lambda x: x[0])
    indexed_correct_attempts.sort(key=lambda x: x[0])
    cut_off = len(qa_data) // 4
    # If the 25% of questions is less than the threshold, grab the entire 25%, otherwise sample from it.
    ratio_candidates = indexed_ratios[:cut_off] if len(indexed_ratios[:cut_off]) < lowestRatio else random.sample(indexed_ratios[:cut_off], lowestRatio)
    correct_attempts_candidates = indexed_correct_attempts[:cut_off] if len(indexed_correct_attempts[:cut_off]) < lowestCorrectAttempts else random.sample(indexed_correct_attempts[:cut_off], lowestCorrectAttempts)
    
    all_indices = list(range(len(qa_data)))
    random_indices = random.sample(all_indices, randomPick)
    ratio_indices = [index for value, index in ratio_candidates]
    correct_attempts_indices = [index for value, index in correct_attempts_candidates]
    selected_indices = list(set(ratio_indices + correct_attempts_indices + random_indices))
    
    return [(qa_data[i]['question'], qa_data[i]['answer']) for i in selected_indices]


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

    return main_list  # Return the full list of question-answer pairs

