import random

# List of random responses to be given after each answer
responses = ["Good job!", "Nice!", "Great!", "Awesome!"]

# List of questions to be asked
questions = ["What's Your Name?", "What's Your Age?", "What's Your Favorite Color?", "What's Your Favorite Hobby?", "What's Your Favorite Movie?"]

# Function to ask a question and provide a random response
def ask_question(question):
    answer = input(question + " ")
    print(random.choice(responses))
    print()  # print a blank line

# Function to randomly ask 2 questions and provide random responses
def random_question():
    print("I'll ask you 2 random questions: ")
    selected_questions = random.sample(questions, 2)  # randomly select 2 questions
    for question in selected_questions:
        ask_question(question)

# Calls the function to start the program
random_question()