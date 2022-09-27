"""
    Student Name: Limor Segal Shevah
    Project: World Of Games
"""
import random
import requests
from Utils import REST_API_SUCCESS_RESPONSE, print_exception_error, get_game_max_difficulty, validate_numeric_input, \
    DictToObject

USD_ILS_EXCHANGE_API_KEY = "c6577bc3f81ed6f02ddeb5ec"
EXCHANGE_API_URL = f"https://v6.exchangerate-api.com/v6/{USD_ILS_EXCHANGE_API_KEY}/latest/USD"
CURRENCEY = "ILS"
MAX_RAND_NUM = 100
money_interval_formula = lambda d, t: range(t - (5 - d), t + (5 - d))


def get_money_interval(difficulty, usd_money_value):
    try:
        response = requests.get(EXCHANGE_API_URL)
        if REST_API_SUCCESS_RESPONSE == response.status_code:
            res_json_object = response.json()
            currency_rate = DictToObject(res_json_object).conversion_rates[CURRENCEY]
            # print(f"currency_rate => {currency_rate}")  # for me to check
            total_money_value = round(currency_rate * usd_money_value)
            return money_interval_formula(difficulty, total_money_value)
    except TypeError as e1:
        print_exception_error(f"TypeError exception: wrong parameter type passed, {e1.args}")
    except BaseException as e2:
        print_exception_error(f"Something went wrong, the following exception occurred: {e2.args}")


def get_guess_from_user(usd_money_value):
    return int(validate_numeric_input(f"Guess :) how much {usd_money_value} USD are in ILS? "))


def play(difficulty_level=None):
    try:
        difficulty = difficulty_level if difficulty_level else get_game_max_difficulty("Currency Roulette")
        usd_money_value = random.randint(1, MAX_RAND_NUM)
        money_interval = get_money_interval(difficulty, usd_money_value)
        user_guess = get_guess_from_user(usd_money_value)
        # print(f"money_interval => {money_interval}")  # for me to check
        if money_interval.start == money_interval.stop:
            return user_guess == money_interval.start
        else:
            return user_guess in money_interval
    except BaseException as e:
        print_exception_error(f"Something went wrong, the following exception occurred: {e.args}")


# print("You won!") if play() else print("You lost!")
# print("You won!") if play(3) else print("You lost!")
