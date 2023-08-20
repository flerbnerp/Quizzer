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
        },
        {
            "question": "How do you properly fetch and pull from an established repository on Github?",
            "answer": "git fetch origin, git pull origin main",
            "correct_attempts": 0, 
            "total_attempts": 0
        },
        {
            "question": "How do you properly push your changes to the Github repository?",
            "answer": "git status, git add ., git commit -m 'message', git push origin main",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "Please describe the concept of Overlearning.",
            "answer": "Overlearning.md",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "Please explain the concept of the Forgetting Curve.",
            "answer": "Forgetting Curve.md",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is programming?",
            "answer": "Programming is the process of creating a set of instructions that tell a computer how to perform a task.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "The name Python in the Python programming language was inspired by what?",
            "answer": "Monty Python",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "In programming, what is an operator?",
            "answer": "An operator is a special symbol that represents a simple computation like addition, multiplication, or string concatenation.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "In programming, what are all the specific operators?",
            "answer": "%, **, *, /, //, +, -",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is the %' operator called?",
            "answer": "The %' operator is called the modulus operator.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What operator is used for remainder division?",
            "answer": "The %' operator is used for remainder division.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is the **' operator called?",
            "answer": "The **' operator is called the exponent operator.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What operator is used for exponentiation?",
            "answer": "The **' operator is used for exponentiation.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is the *' operator called?",
            "answer": "The *' operator is called the multiplication operator.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What operator is used for multiplication?",
            "answer": "The *' operator is used for multiplication.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is the /' operator called?",
            "answer": "The /' operator is called the division operator.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What operator is used for division?",
            "answer": "The /' operator is used for division.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is the //' operator called?",
            "answer": "The //' operator is called the floor division operator.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What operator is used for floor division?",
            "answer": "The //' operator is used for floor division.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is the +' operator called?",
            "answer": "The +' operator is called the addition operator.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What operator is used for addition?",
            "answer": "The +' operator is used for addition.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is the -' operator called?",
            "answer": "The -' operator is called the subtraction operator.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What operator is used for subtraction?",
            "answer": "The -' operator is used for subtraction.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is floor division?",
            "answer": "Floor division is a normal division operation except that it returns the largest possible integer. Ignoring fractions.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is the difference between the /' and //' operators?",
            "answer": "The /' operator returns a floating point number, while the //' operator returns an integer.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "Please give a list of all data types in Python.",
            "answer": "int, float, str, bool, list, tuple, dict, set, frozenset, complex, bytes, bytearray, range, None",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is an int or integer data type?",
            "answer": "An int or integer data type is a whole number, positive or negative, without decimals, of unlimited length.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a float or floating point data type?",
            "answer": "A float or floating point data type is a number, positive or negative, containing one or more decimals.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a str or string data type?",
            "answer": "A str or string data type is a sequence of characters, either as a literal constant or as some kind of variable.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a bool or boolean data type?",
            "answer": "A bool or boolean data type is a data type with one of two possible values: True or False.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a list data type?",
            "answer": "A list data type is a collection which is ordered and changeable. Allows duplicate members.",
            "correct_attempts": 0,
            "total_attempts": 0            
        },
        {
            "question": "What is a tuple data type?",
            "answer": "A tuple data type is a collection which is ordered and unchangeable. Allows duplicate members.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a dict or dictionary data type?",
            "answer": "A dict or dictionary data type is a collection which is unordered, changeable and indexed. No duplicate members.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a set data type?",
            "answer": "A set data type is a collection which is unordered and unindexed. No duplicate members.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a frozenset data type?",
            "answer": "A frozenset data type is a collection which is unordered and unindexed. No duplicate members. Immutable.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a complex data type?",
            "answer": "A complex data type is a number, positive or negative, containing one or more decimals. Written with a j as the imaginary part.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "Provide an example of a complex data type.",
            "answer": "x = 3+5j",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a bytes data type?",
            "answer": "A bytes data type is a data type that stores an immutable sequence of numbers in the range 0 <= x < 256.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a bytearray data type?",
            "answer": "A bytearray data type is a data type that stores a mutable sequence of numbers in the range 0 <= x < 256.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a range data type?",
            "answer": "A range data type is a data type that stores an immutable sequence of numbers.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a None data type?",
            "answer": "A None data type is a data type that stores a None value.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a variable?",
            "answer": "A variable is a container for storing a value.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "How do you comment out a block of code all at once in VSCode?",
            "answer": "Highlight the block of code and press Ctrl + /",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is an imaginary number? Explain at length.",
            "answer": "An imaginary number is a number that is expressed in terms of the square root of a negative number (usually the square root of -1, which is represented by the letter i). Imaginary numbers are used in complex numbers, which are used to solve problems in electrical engineering and physics.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "When was the term imaginary number first used? By whom?",
            "answer": "The term imaginary number was first used in the 17th century by René Descartes.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is string concatenation? and how is it done?",
            "answer": "String concatenation is the process of joining two or more strings together to create a new string. It is done by using the + operator.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is the difference between the + and * operators when used with strings?",
            "answer": "The + operator is used to concatenate strings, while the * operator is used to repeat strings.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is a variable name? What makes it valid or invalid?",
            "answer": "A variable name is the name given to a variable. A variable name must start with a letter or the underscore character. A variable name cannot start with a number. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ). Variable names are case-sensitive (age, Age and AGE are three different variables).",
            "correct_attempts": 0,
            "total_attempts": 0        
        },
        {
            "question": "What is camelcase? and why is it used?",
            "answer": "Camelcase is a naming convention in which a name is formed of multiple words that are joined together as a single word with the first letter of each of the multiple words capitalized so that each word that makes up the name can easily be read. It is used to make variable names easier to read.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is snakecase? and why is it used?",
            "answer": "Snakecase is a naming convention in which a name is formed of multiple words that are joined together as a single word with an underscore between each of the multiple words so that each word that makes up the name can easily be read. It is used to make variable names easier to read.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "In programming, what is a comment? Why is it used?",
            "answer": "A comment is a line of code that is not executed by the interpreter. It is used to explain what the code is doing.",
            "correct_attempts": 0,
            "total_attempts": 0            
        },
        {
            "question": "In Python? What is the print function? Please provide an example of proper syntax.",
            "answer": "The print function is a built-in function that prints the specified message to the screen. print('Hello, World!')",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "In Python? What is the input function? Please provide an example of proper syntax.",
            "answer": "The input function is a built-in function that prompts the user for input and returns the input as a string. input('What is your name?')",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What data type is user input evaluated to?",
            "answer": "User input is evaluated to a string data type.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "How do you convert a string to an integer?",
            "answer": "int('3')",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "How long can a source code document be?",
            "answer": "A source code document can be as long as you want it to be.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "Can an integer be negative?",
            "answer": "Yes, an integer can be negative.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is the difference between indexed and unindexed collections",
            "answer": "Indexed collections are collections that are ordered and can be accessed by their index. Unindexed collections are collections that are unordered and cannot be accessed by their index.",
            "correct_attempts": 0,
            "total_attempts": 0
        },
        {
            "question": "What is the use case for an unindexed unordered collection?",
            "answer": "An unindexed unordered collection is useful when you want to store a collection of unique items.",
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
