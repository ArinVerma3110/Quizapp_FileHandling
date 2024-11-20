# Name : Arin Verma
# Enrollment No. : 0176AL221031

# Assignment 2       Submission Date : 18/11/24


# Q2. Program of quiz app using file handling

import random

USER_FILE = "users.txt"
QUESTION_FILE = "questions.txt"

def register_user():
    with open(USER_FILE, "a+") as file:
        username = input("Enter a username: ").strip()
        file.seek(0)
        if any(line.split()[0] == username for line in file):
            print("Username already exists. Try again.")
            return register_user()
        password = input("Enter a password: ").strip()
        file.write(f"{username} {password}\n")
        print("User registered successfully!")


def login_user():
    with open(USER_FILE, "r") as file:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        for line in file:
            stored_user, stored_pass = line.strip().split()
            if username == stored_user and password == stored_pass:
                print("Login successful!")
                return True
        print("Invalid username or password. Try again.")
        return False

# Function jisse file se questions load karwa lu
def load_questions():
    topics = {}
    with open(QUESTION_FILE, "r") as file:
        for line in file:
            topic, question, correct, *options = line.strip().split("|")
            if topic not in topics:
                topics[topic] = []
            topics[topic].append((question, correct, options))
    return topics


def start_quiz(topics):
    print("\nAvailable topics:", ", ".join(topics.keys()))
    selected_topic = input("Select a topic: ").strip().capitalize()
    if selected_topic not in topics:
        print("Invalid topic selected!")
        return start_quiz(topics)

    questions = random.sample(topics[selected_topic], 5)
    score = 0

    for question, correct, options in questions:
        print(f"\n{question}")
        all_options = options + [correct]
        random.shuffle(all_options)
        for i, option in enumerate(all_options, 1):
            print(f"{i}. {option}")
        try:
            user_answer = int(input("Choose the correct answer : "))
            if all_options[user_answer - 1].strip() == correct.strip():
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer was: {correct}")
        except (ValueError, IndexError):
            print("Invalid input. Moving to the next question.")

    print(f"\nYou scored {score} out of 5.\n")

# Main function
def main():
    print("Welcome to the Quiz Application!")
    while True:
        choice = input("Do you want to (1) Register or (2) Login? Enter 1 or 2: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            if login_user():
                break

    topics = load_questions()
    while True:
        start_quiz(topics)
        retry = input("Do you want to (1) Retry or (2) Exit? Enter 1 or 2: ")
        if retry == "2":
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()