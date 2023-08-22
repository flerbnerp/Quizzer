import random
import os
import json
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

def find_and_update_question_entry(unique_id, question, answer, filename, image_path_question=None, image_path_answer=None):
    with open(filename, 'r') as file:
        questions = json.load(file)

    for question_entry in questions:
        if question_entry.get("unique_id") == unique_id:
            question_entry["question"] = question
            question_entry["answer"] = answer
            if image_path_question:
                question_entry["image_path_question"] = image_path_question
            if image_path_answer:
                question_entry["image_path_answer"] = image_path_answer
            break

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

    # Generate visualization for the question
    plt.figure(figsize=(6, 4))
    plt.text(0.5, 0.5, f"{num1} + {num2} = x", ha='center', va='center', fontsize=15)
    plt.axis('off')
    
    image_directory = "matLabImages"
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)
    function_name = generate_addition_question.__name__
    image_path_question = os.path.join(image_directory, f"{function_name}_question.png")

    plt.savefig(image_path_question, bbox_inches="tight", pad_inches=0)
    plt.close()

    # As we're not generating a separate image for the answer in this case, we will not create an image_path_answer
    unique_id = "math0004"
    filename = "qaJsonFiles/qaMathematics.json"
    find_and_update_question_entry(unique_id, question, answer, filename, image_path_question=image_path_question)

    return question, answer, image_path_question

def generate_rational_number_question():
    num1 = random.randint(0, 9999)
    correct_answer = f"{num1}\n---\n  1"

    question = f"Please write the following number as a rational number:\n\n{num1}"
    answer = str(correct_answer)

    unique_id = "math0005"
    filename = "qaJsonFiles/qaMathematics.json"

    # Create Matplotlib figure for the rational number answer
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.text(0.5, 0.6, str(num1), ha='center', va='center', fontsize=20)
    ax.text(0.5, 0.4, "1", ha='center', va='center', fontsize=20)
    ax.plot([0.3, 0.7], [0.5, 0.5], color="black")
    ax.axis("off")

    # Determine the image path for the answer based on the function's name
    image_directory = "matLabImages"
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)
    function_name = generate_rational_number_question.__name__
    image_path_answer = os.path.join(image_directory, f"{function_name}_answer.png")

    # Save the image and close the plot
    plt.savefig(image_path_answer, bbox_inches="tight", pad_inches=0)
    plt.close()

    # Update the question entry with the image path for the answer
    find_and_update_question_entry(unique_id, question, answer, filename, image_path_answer=image_path_answer)

    return question, answer, image_path_answer

def generateWriteAsEitherTerminatingOrRepeatingDecimal():
    num1 = random.randint(0, 9999)
    num2 = random.randint(0, 9999)
    result = num1 / num2
    digits = count_decimal_digits(result)
    if digits > 7:
        correct_answer = "repeating"
    else:
        correct_answer = "terminating"
        
    fraction_representation = f"{num1}/{num2}"
    question = f"Please write the following number as either a terminating or repeating decimal:\n\n{fraction_representation}"
    answer = str(correct_answer)
    
    # Create Matplotlib figure for the fraction
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.text(0.5, 0.6, str(num1), ha='center', va='center', fontsize=20)
    ax.text(0.5, 0.4, str(num2), ha='center', va='center', fontsize=20)
    ax.plot([0.3, 0.7], [0.5, 0.5], color="black")
    ax.axis("off")

    # Determine the image path for the question based on the function's name
    image_directory = "matLabImages"
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)
    function_name = generateWriteAsEitherTerminatingOrRepeatingDecimal.__name__
    image_path_question = os.path.join(image_directory, f"{function_name}_question.png")

    # Save the image and close the plot
    plt.savefig(image_path_question, bbox_inches="tight", pad_inches=0)
    plt.close()

    unique_id = "math0006"  
    filename = "qaJsonFiles/qaMathematics.json"
    
    # Update the question entry with the image path for the question
    find_and_update_question_entry(unique_id, question, answer, filename, image_path_question=image_path_question)
    
    return question, answer, image_path_question


def run_all_generators():
    generate_addition_question()
    generate_rational_number_question()
    generateWriteAsEitherTerminatingOrRepeatingDecimal()
    # Add more generators here