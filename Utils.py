"""
    Student Name: Limor Segal Shevah
    Project: World Of Games
"""
from inspect import getframeinfo, stack
import ast
import json
import os

###############
# Definitions #
###############
# Games related
GAMES_CONFIG_FILE = "games_config.json"
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1
SUCCESS_RETURN_CODE = 0
MAX_SCORE = 1000

# General
REST_API_SUCCESS_RESPONSE = 200
# File open modes
WRITE_FILE_MODE = "w"
READ_FILE_MODE = "r"


class DictToObject(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


def dict_to_object(d):
    return json.loads(json.dumps(d), object_hook=DictToObject)


def get_config_dict(file):
    try:
        config_file = open(file, READ_FILE_MODE)
        json_object = dict(ast.literal_eval(config_file.read()))
        config_file.close()
        return json_object
    except IOError:
        raise FileNotFoundError(f"{file} does not exist in your system! program will exit...")
    except BaseException as e:
        print_exception_error(f"Something went wrong, the following exception occurred {e.args}")


def where_exception(func):
    def wrapper(e):
        print("----------------------------------------------")
        caller = getframeinfo(stack()[1][0])
        print(f"Python exception occurred in {caller.filename} {caller.lineno}")
        func(e)
        print("----------------------------------------------")
    return wrapper


@where_exception
def print_exception_error(error, force_exit=False):
    print(error)
    if force_exit:
        print("This is critical error! program is terminated!")
        exit(1)


@where_exception
def print_exception_error(error):
    print(error)


def validate_int_range_input(input_message, max_int):
    try:
        valid_options = [str(x) for x in range(1, max_int + 1)]
        user_selection = input(input_message)
        choose_msg = input_message.split('\n')[0]
        while user_selection not in valid_options:
            user_selection = input(f"Invalid option! the input suppose to be a number between 1 to {len(valid_options)}"
                                   f",{choose_msg}")
        return user_selection
    except TypeError as e1:
        print_exception_error(f"TypeError exception: wrong parameter (valid_options) type passed, {e1.args}")
    except BaseException as e2:
        print_exception_error(f"Something was wrong, exception occurred: {e2.args}")


def validate_numeric_input(input_message):
    try:
        user_selection = input(input_message)
        while not user_selection.isnumeric():
            user_selection = input("You did not enter any number, please try again: ")
        return user_selection
    except TypeError as e1:
        print_exception_error(f"TypeError exception: wrong parameter (valid_options) type passed, {e1.args}")
    except BaseException as e2:
        print_exception_error(f"Something was wrong, exception occurred: {e2.args}")


def get_game_json_object(game_name):
    try:
        games_json_object = DictToObject(get_config_dict(GAMES_CONFIG_FILE))
        for game in games_json_object.games:
            game_object = DictToObject(game)
            if game_object.name == game_name:
                return game_object
        print(f"Game {game_name} does not exist!")
    except BaseException as e:
        print_exception_error(f"Something was wrong, exception occurred: {e.args}")


def get_game_max_difficulty(game_name):
    try:
        game_json_block = get_game_json_object(game_name)
        game_json_object = DictToObject(game_json_block)
        if game_json_object:
            return int(game_json_object.difficulty)
    except TypeError as e1:
        print_exception_error(f"TypeError exception: wrong parameter type passed, {e1.args}")
    except BaseException as e2:
        print_exception_error(f"Something was wrong, exception occurred: {e2.args}")


def screen_cleaner():
    os.system("cls")
