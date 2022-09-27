"""
    Student Name: Limor Segal Shevah
    Project: World Of Games
"""
import os
import random
from time import sleep
from Utils import validate_int_range_input, get_game_max_difficulty, print_exception_error

MAX_GUESS_VALUE = 100
MIN_GUESS_VALUE = 1


def generate_sequence(difficulty):
    try:
        random_sequence = random.sample(range(MAX_GUESS_VALUE + 1), difficulty)
        print(random_sequence)
        sleep(0.7)
        os.system("cls")
        return random_sequence
    except ValueError as e1:
        print_exception_error(f"Difficulty must be non-negative number: {e1.args}")
    except TypeError as e2:
        print_exception_error(f"TypeError exception: wrong parameter (difficulty) type passed, {e2.args}")
    except BaseException as e3:
        print_exception_error(f"Something went wrong, the following exception occurred: {e3.args}")


def get_list_from_user(difficulty):
    try:
        return [int(validate_int_range_input(f"Enter an integer number between {MIN_GUESS_VALUE} to {MAX_GUESS_VALUE}:",
                                             MAX_GUESS_VALUE)) for _ in range(difficulty)]
    except TypeError as e1:
        print_exception_error(f"TypeError exception: wrong parameter (difficulty) type passed, {e1.args}")
    except BaseException as e2:
        print_exception_error(f"Something went wrong, the following exception occurred: {e2.args}")


def is_list_equal(l1, l2):
    try:
        return sorted(l1) == sorted(l2)
    except TypeError as e1:
        print_exception_error(f"TypeError exception: wrong parameter type passed, {e1.args}")
    except BaseException as e2:
        print_exception_error(f"Something went wrong, the following exception occurred: {e2.args}")


def play(difficulty_level=None):
    difficulty = difficulty_level if difficulty_level else get_game_max_difficulty("Memory Game")
    sys_picked_list = generate_sequence(difficulty)
    user_guess_list = get_list_from_user(difficulty)
    return is_list_equal(sys_picked_list, user_guess_list)
