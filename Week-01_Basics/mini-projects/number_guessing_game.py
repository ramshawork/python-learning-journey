import random  # Python ka random module


def number_guessing_game():  # will work on function its a professional way
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    low = 1
    high = 100

    while True:
        # user_guess = input("Enter your guess:")
        user_input = input(f"Guess a number between {low} and {high}: ")

        if not user_input.isdigit():
            print("Please enter a valid number")
            continue

        user_guess = int(user_input)
        attempts += 1

        if user_guess < secret_number:
            print("Too low! Try a higher number.")
            low = user_guess + 1  # next guess minimum
        elif user_guess > secret_number:
            print("Too high! Try a lower number.")
            high = user_guess - 1  # next guess maximum
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break


# CALLING THE FUNCTION TO START GAME
number_guessing_game()


# Logic Steps:
# Random number generate karna hai
# User se input lena hai
# Compare karna hai
# Feedback dena hai
# Loop tab tak chalana hai jab tak correct na ho
# Guesses count karna hai


# SUMMARY
# Input string user_input me store hoti hai
# .isdigit() check user_input pe hona chahiye, user_guess pe nahi
# Uske baad string → int convert karta hai
# Hints low/high → user ko clear guidance
# Attempts count → beginner mistakes avoid karne me help
