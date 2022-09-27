"""
    Student Name: Limor Segal Shevah
    Project: World Of Games
"""
from inspect import getframeinfo, stack
from Utils import get_config_dict, dict_to_object
from Score import add_score

import CurrencyRouletteGame
import MemoryGame
import GuessGame

games_config_file = "games_config.json"


def where_exception(func):
    def wrapper(e):
        print("----------------------------------------------")
        caller = getframeinfo(stack()[1][0])
        print(f"Python exception occurred in {caller.filename} {caller.lineno}")
        func(e)
        print("----------------------------------------------")
    return wrapper


@where_exception
def print_exception_error(error):
    print(error)


def generate_list_of_str_nums(num):
    return [str(x) for x in range(1, num + 1)]


def validate_input(input_message, valid_options):
    try:
        user_selection = input(input_message)
        choose_msg = input_message.split('\n')[0]
        while user_selection not in valid_options:
            user_selection = input(f"Invalid option! the input suppose to be a number between 1 to {len(valid_options)}"
                                   f",{choose_msg}")
        return user_selection
    except TypeError as e:
        print_exception_error(f"TypeError exception: wrong parameter (valid_options) type passed, {e.args}")
    except BaseException as e:
        print_exception_error(f"Something was wrong, exception occurred: {e.args}")


def welcome(name):
    try:
        config_object = dict_to_object(get_config_dict(games_config_file))
        return config_object.welcome_msg.replace("<name>", str(name))
    except KeyError as e1:
        print_exception_error(f"Key error when parsing file {games_config_file}, missing key: {e1.args[0]}")
    except BaseException as e2:
        print_exception_error(f"Something went wrong, the following exception occurred: {e2.args}")


def load_game():
    try:
        game_config_object = dict_to_object(get_config_dict(games_config_file))
        choose_game_msg = game_config_object.game_choice_msg
        games_menu = ''
        games_list = game_config_object.games
        num_of_games = len(games_list)
        if num_of_games > 0:
            valid_games_options = generate_list_of_str_nums(num_of_games)
            for i in valid_games_options:
                game_info = games_list[int(i) - 1]  # List start from 0
                games_menu += f"{i}. {game_info.name} - {game_info.instructions}\n"
            chosen_game = validate_input(f"{choose_game_msg}\n{games_menu}", valid_games_options)
            chosen_game_list_idx = int(chosen_game) - 1
            game_num_of_levels = games_list[chosen_game_list_idx].difficulty
            game_valid_difficulty_levels = generate_list_of_str_nums(int(game_num_of_levels))  # List start
            chosen_difficulty_level = validate_input(f"{game_config_object.difficulty_choice_msg}{game_num_of_levels}"
                                                     f":", game_valid_difficulty_levels)  # Requested to keep it to a
            selected_game_source = games_list[chosen_game_list_idx].game_source
            game_result = eval(selected_game_source + f".play({chosen_difficulty_level})")
            if game_result:
                print("You won!")
                add_score(chosen_difficulty_level)
            else:
                print("You lost!")
        else:
            print("No games are currently available!")
    except KeyError as e1:
        print_exception_error(f"Key error exception occurred, key '{e1.args[0]}' does not exist in JSON parsed")
    except BaseException as e2:
        print_exception_error(f"Something went wrong, the following exception occurred: {e2.args}")
