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
    print(f"\nQuestion {question_counter + 1}: {questions[question_counter]}")
    
    for i in range(4):
        print(f"{i + 1}: {options[question_counter][i]}")

# User data function

def get_user_answer():
    while True:
        user_input = input("Your answer (1/2/3/4): ")

        if user_input.isdigit() and 1 <= int(user_input) <= 4:
            return int(user_input)
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4.")

# Checking the answer

def check_answer(user_answer):
    global score

    if user_answer == answers[question_counter]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")


