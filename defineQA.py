import json

QA_FILE = "qa.json"

def define_questions_and_answers():
    """
    Define a list of question and answer pairs.
    """
    qa_pairs = [
        {
            "question": "What is Python?",
            "answer": "Python is a programming language.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "Describe Active Recall?",
            "answer": "Active Recall.md",
            "correct_attempts": 0,
            "total_attempts": 0            
        },
        {
            "question": "Describe Spaced Repetition?",
            "answer": "Spaced Repetition.md",
            "correct_attempts": 0,
            "total_attempts": 0            
        },
        {
            "question": "Describe Interleaving?",
            "answer": "Interleaving.md",
            "correct_attempts": 0,
            "total_attempts": 0            
        },
        {
            "question": "What are the three core concepts of learning in a scientific manner?",
            "answer": "Active Recall, Spaced Repetition, and Interleaving.",
            "correct_attempts": 0,
            "total_attempts": 0        
        }
    ]

    return qa_pairs

def write_to_qa_file(qa_pairs):
    """
    Write the provided question and answer pairs to qa.json.
    """
    existing_data = []

    # Check if the QA_FILE already exists and if so, load its contents.
    try:
        with open(QA_FILE, 'r') as file:
            file_content = file.read()
            if file_content:  # Check for non-empty content
                existing_data = json.loads(file_content)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    # Create a set of existing questions for quick lookup.
    existing_questions = {item['question'] for item in existing_data}

    # Append new questions to the existing data.
    for pair in qa_pairs:
        if pair['question'] not in existing_questions:
            existing_data.append(pair)

    # Save combined data back to the file.
    with open(QA_FILE, 'w') as file:
        json.dump(existing_data, file, indent=4)
def setup_qa():
    qa_data = define_questions_and_answers()
    write_to_qa_file(qa_data)

if __name__ == "__main__":
    qa_data = define_questions_and_answers()
    write_to_qa_file(qa_data)
    print(f"Questions and answers saved to {QA_FILE}.")
