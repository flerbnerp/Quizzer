import random
import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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
def count_decimal_digits(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Find the position of the decimal point
    decimal_point_index = number_str.find('.')
    
    # If there is no decimal point, return 0
    if decimal_point_index == -1:
        return 0
    
    # Count the digits after the decimal point
    digits_after_decimal = len(number_str) - decimal_point_index - 1
    
    return digits_after_decimal
        
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

def generate_rational_number_question():
    num1 = random.randint(0, 9999)
    correct_answer = f"{num1}\n---\n  1"

    question = f"Please write the following number as a rational number:\n\n{num1}"
    answer = str(correct_answer)

    unique_id = "math0005"  # Replace this with the actual unique ID
    filename = "qaJsonFiles/qaMathematics.json"  # Replace with the correct file path

    find_and_update_question_entry(unique_id, question, answer, filename)

    return question, answer

def generateWriteAsEitherTerminatingOrRepeatingDeciaml():
    num1 = random.randint(0, 9999)
    num2 = random.randint(0, 9999)
    result = num1 / num2
    digits = count_decimal_digits(result)
    if digits > 7:
        correct_answer = "repeating"
    else:
        correct_answer = "terminating"
        
    question = f"Please write the following number as either a terminating or repeating decimal:\n\n{result}"
    answer = str(correct_answer)
    
    unique_id = "math0006"  # Replace this with the actual unique ID
    filename = "qaJsonFiles/qaMathematics.json"  # Replace with the correct file path
    
    find_and_update_question_entry(unique_id, question, answer, filename)
    
    return question, answer

def run_all_generators():
    generate_addition_question()
    generate_rational_number_question()
    generateWriteAsEitherTerminatingOrRepeatingDeciaml()
    # Add more generators here