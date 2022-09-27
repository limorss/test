"""
    Student Name: Limor Segal Shevah
    Project: World Of Games
"""
from Live import load_game, welcome
from Utils import screen_cleaner

if __name__ == "__main__":
    print(welcome("Guy"))
    choice = None
    while "0" != choice:
        load_game()
        choice = input(f"Do you want to continue to a new game? ('0': Exit, 'Enter': continue)")
        screen_cleaner()
