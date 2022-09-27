"""
    Student Name: Limor Segal Shevah
    Project: World Of Games
"""
from random import randint
from Utils import validate_int_range_input, get_game_max_difficulty, print_exception_error


def generate_number(difficulty):
    try:
        secret_number = randint(1, difficulty)
        return secret_number
    except ValueError as e1:
        print_exception_error(f"Difficulty must be non-negative number: {e1.args}")
    except TypeError as e2:
        print_exception_error(f"TypeError exception: wrong parameter type passed, {e2.args}")
    except BaseException as e3:
        print_exception_error(f"Something went wrong, the following exception occurred: {e3.args}")


def get_guess_from_user(difficulty):
    return validate_int_range_input(f"Enter an integer number between 1 to {difficulty}",
                                    difficulty)


def compare_results(secret_number, guessed_number):
    return secret_number == guessed_number


def play(difficulty_level=None):
    difficulty = difficulty_level if difficulty_level else get_game_max_difficulty("Guess Game")
    secret_number = generate_number(difficulty)
    # print(secret_number)  # for me to check
    user_guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, int(user_guess))


# print("You won!") if play(4) else print("You lost!")
# print("You won!") if play() else print("You lost!")
