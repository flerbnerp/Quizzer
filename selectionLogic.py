import json
import random

QA_FILE = "qa.json"

def get_weighted_question():
    with open(QA_FILE, 'r') as file:
        qa_data = json.load(file)
    
    # Calculate ratios and store them along with their indices
    indexed_ratios = []
    for index, qa in enumerate(qa_data):
        total_attempts = qa.get("total_attempts", 0)
        correct_attempts = qa.get("correct_attempts", 0)
        ratio = 0 if total_attempts == 0 else correct_attempts / total_attempts
        indexed_ratios.append((ratio, index))
    
    # Sort by ratio
    indexed_ratios.sort(key=lambda x: x[0])
    
    # Collect candidates until we have at least 5 or have exhausted the list
    candidates = []
    i = 0
    while len(candidates) < 5 and i < len(indexed_ratios):
        current_ratio = indexed_ratios[i][0]
        candidates.extend([x[1] for x in indexed_ratios if x[0] == current_ratio])
        i += 1

    # Randomly choose a question from the candidates
    selected_index = random.choice(candidates)

    return qa_data[selected_index]['question'], qa_data[selected_index]['answer']

if __name__ == "__main__":
    question, answer = get_weighted_question()
    print("Question:", question)
    print("Answer:", answer)
