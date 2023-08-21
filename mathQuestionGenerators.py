import random
import json

def find_and_update_question_entry(unique_id, question, answer, filename):
    with open(filename, 'r') as file:
        questions = json.load(file)

    for question_entry in questions:
        if question_entry.get("unique_id") == unique_id:
            question_entry["question"] = question
            question_entry["answer"] = answer
            break  # No need to continue searching

    with open(filename, 'w') as file:
        json.dump(questions, file, indent=4)
        
def generate_addition_question():
    num1 = random.randint(0, 9999)
    num2 = random.randint(0, 9999)
    correct_answer = num1 + num2

    question = f"Solve for x:\n\n{num1} + {num2} = x"
    answer = str(correct_answer)

    unique_id = "math0004"  # Replace this with the actual unique ID
    filename = "qaJsonFiles/qaMathematics.json"  # Replace with the correct file path

    find_and_update_question_entry(unique_id, question, answer, filename)

    return question, answer

def run_all_generators():
    generate_addition_question()
    # Add more generators here