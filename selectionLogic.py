import json
import random
import os
from mathQuestionGenerators import run_all_generators

QA_DIR = "qaJsonFiles"

def get_files_in_directory(directory, prefix):
    """Get all files in a directory with a specific prefix."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.startswith(prefix)]

def select_question_from_file(filepath):
    with open(filepath, 'r') as file:
        qa_data = json.load(file)

    indexed_ratios = []
    for index, qa in enumerate(qa_data):
        total_attempts = qa.get("total_attempts", 0)
        correct_attempts = qa.get("correct_attempts", 0)
        ratio = 0 if total_attempts == 0 else correct_attempts / total_attempts
        indexed_ratios.append((ratio, index))

    indexed_ratios.sort(key=lambda x: x[0])

    candidates = [x[1] for x in indexed_ratios[:10]]

    all_indices = list(range(len(qa_data)))
    
    # Number of random samples depends on the length of qa_data
    num_samples = min(3, len(qa_data))
    random_indices = random.sample(all_indices, num_samples)

    candidates.extend(random_indices)
    selected_index = random.choice(candidates)

    return qa_data[selected_index]['question'], qa_data[selected_index]['answer']

def get_weighted_question():
    run_all_generators()
    qa_files = get_files_in_directory(QA_DIR, "qa")
    random.shuffle(qa_files)

    # Use all available files if less than 5, otherwise use 5.
    num_files_to_use = min(len(qa_files), 5)

    main_list = []
    for i in range(num_files_to_use):
        question, answer = select_question_from_file(os.path.join(QA_DIR, qa_files[i]))
        main_list.append((question, answer, os.path.join(QA_DIR, qa_files[i])))

    return main_list  # Return the full list of question-answer pairs

