# Implementing the question_bank

questions = {
    0: "What is the capital of France?",
    1: "Which data structure uses key-value pairs?",
    2: "What is 5 + 7?",
    3: "Which planet is known as the Red Planet?",
    4: "Which language is used to create web pages?"
}

options = {
    0: ["London", "Paris", "Berlin", "Madrid"],
    1: ["List", "Tuple", "Dictionary", "Set"],
    2: ["10", "11", "12", "13"],
    3: ["Earth", "Mars", "Jupiter", "Venus"],
    4: ["Python", "HTML", "Java", "C++"]
}

answers = {
    0: 2,
    1: 3,
    2: 3,
    3: 2,
    4: 2
}

# Implementing other useful variables

score = 0
question_counter = 0
total_questions = len(questions)

# Display question function

def display_question():
    print(f"\nQuestion {question_counter + 1}: {questions[question_counter]}")
    print("1:", options[question_counter][0])
    print("2:", options[question_counter][1])
    print("3:", options[question_counter][2])
    print("4:", options[question_counter][3])

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
