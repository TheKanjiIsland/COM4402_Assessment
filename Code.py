# Implementing the question_bank

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which data structure uses key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Dictionary"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "Which language is used to create web pages?",
        "options": ["Python", "HTML", "Java", "C++"],
        "answer": "HTML"
    }
]

# Implementing other useful variables

score = 0
question_counter = 0
total_questions = len(questions)

# Display question function

def display_question():
    print(f"\nQuestion {question_counter + 1}: {questions[question_counter]['question']}")
    
    for i in range(len(questions[question_counter]['options'])):
        print(f"{i + 1}: {questions[question_counter]['options'][i]}")

# User data function

def get_user_number_in_range(min_val, max_val):
    valid_options = questions[question_counter]['options']
    while True:
        user_input = input("Your answer (type exactly as shown): ")
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please type one of the options exactly as displayed.")

# Checking the answer

def check_answer(user_answer):
    global score

    if user_answer == questions[question_counter]['answer']:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")

# Moving on to the next question

def next_question():
    global question_counter
    question_counter += 1






