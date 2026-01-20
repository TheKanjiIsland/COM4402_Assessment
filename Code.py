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
    0: "2",
    1: "3",
    2: "3",
    3: "2",
    4: "2"
}

# Implementing other useful variables

score = 0
question_counter = 0
total_questions = len(questions)
