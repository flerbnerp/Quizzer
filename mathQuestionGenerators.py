import random
import json
from sympy import symbols, simplify
##############################################################################################################
# Helper Functions
def find_and_update_question_entry(unique_id, question, answer, filename, image_path_question=None, image_path_answer=None):
    with open(filename, 'r') as file:
        questions = json.load(file)
    for question_entry in questions:
        if question_entry.get("unique_id") == unique_id:
            question_entry["question"] = question
            question_entry["answer"] = answer
            break
    with open(filename, 'w') as file:
        json.dump(questions, file, indent=4)

def count_decimal_digits(number):
    number_str = str(number)
    decimal_point_index = number_str.find('.')
    if decimal_point_index == -1:
        return 0
    digits_after_decimal = len(number_str) - decimal_point_index - 1
    return digits_after_decimal
##############################################################################################################
# Question Generators
def generate_multiplication_question():
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    correct_answer = num1 * num2
    question = f"Solve for x:\n\n{num1} x {num2} = x"
    answer = str(correct_answer)
    unique_id = "math0011"
    filename = "qaJsonFiles/qaMathematics.json"
    find_and_update_question_entry(unique_id, question, answer, filename)
    return question, answer

def generate_addition_question():
    num1 = random.randint(0, 9999)
    num2 = random.randint(0, 9999)
    correct_answer = num1 + num2
    question = f"Solve for x:\n\n{num1} + {num2} = x"
    answer = str(correct_answer)
    unique_id = "math0004"
    filename = "qaJsonFiles/qaMathematics.json"
    find_and_update_question_entry(unique_id, question, answer, filename)
    return question, answer

def generate_rational_number_question():
    num1 = random.randint(0, 9999)
    correct_answer = f"{num1}\n---\n  1"
    question = f"Please write the following number as a rational number:\n\n{num1}"
    answer = str(correct_answer)
    unique_id = "math0005"
    filename = "qaJsonFiles/qaMathematics.json"
    find_and_update_question_entry(unique_id, question, answer, filename)
    return question, answer

def generateWriteAsEitherTerminatingOrRepeatingDecimal():
    num1 = random.randint(0, 50)
    num2 = random.randint(1, 50)
    result = num1 / num2
    digits = count_decimal_digits(result)
    if digits > 7:
        correct_answer = "repeating"
    else:
        correct_answer = "terminating"  
    fraction_representation = f"{num1} \n --- \n {num2}"
    question = f"Please write the following number as either a terminating or repeating decimal:\n\n{fraction_representation}"
    answer = str(correct_answer)
    unique_id = "math0006"  
    filename = "qaJsonFiles/qaMathematics.json"
    find_and_update_question_entry(unique_id, question, answer, filename)
    return question, answer

def run_all_generators():
    generate_addition_question()
    generate_multiplication_question()
    generate_rational_number_question()
    generateWriteAsEitherTerminatingOrRepeatingDecimal()
    # Add more generators here