import json

QA_FILE = "qa.json"

def define_questions_and_answers():
    """
    Define a list of question and answer pairs.
    """
    qa_pairs = [
        {
            "question": "What is Python?",
            "answer": "Python is a programming language."
        },
        {
            "question": "Describe Active Recall?",
            "answer": "Active Recall.md"
        },
        {
            "question": "Describe Spaced Repetition?",
            "answer": "Spaced Repetition.md"
        },
        {
            "question": "Describe Interleaving?",
            "answer": "interleaving.md"
        },
        {
            "question": "What are the three core concepts of learning in a scientific manner?",
            "answer": "Active Recall, Spaced Repetition, and Interleaving."
        }
    ]

    return qa_pairs

def write_to_qa_file(qa_pairs):
    """
    Write the provided question and answer pairs to qa.json.
    """
    with open(QA_FILE, 'w') as file:
        json.dump(qa_pairs, file, indent=4)
def setup_qa():
    qa_data = define_questions_and_answers()
    write_to_qa_file(qa_data)

if __name__ == "__main__":
    qa_data = define_questions_and_answers()
    write_to_qa_file(qa_data)
    print(f"Questions and answers saved to {QA_FILE}.")
