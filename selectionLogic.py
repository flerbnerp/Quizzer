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

    indexed_ratios = []
    for index, qa in enumerate(qa_data):
        total_attempts = qa.get("total_attempts", 0)
        correct_attempts = qa.get("correct_attempts", 0)
        ratio = 0 if total_attempts == 0 else correct_attempts / total_attempts
        indexed_ratios.append((ratio, index))

    indexed_ratios.sort(key=lambda x: x[0])

    candidates = [x[1] for x in indexed_ratios[:5]]

    all_indices = list(range(len(qa_data)))

    # Number of random samples depends on the length of qa_data
    num_samples = min(1, len(qa_data))
    random_indices = random.sample(all_indices, num_samples)
    candidates.extend(random_indices)
    
    # Ensure unique selection
    selected_indices = random.sample(candidates, min(num_questions_to_pick, len(candidates)))
    
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

