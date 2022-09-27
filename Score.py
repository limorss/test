"""
    Student Name: Limor Segal Shevah
    Project: World Of Games
"""
from Utils import SCORES_FILE_NAME, READ_FILE_MODE, WRITE_FILE_MODE, print_exception_error
points_of_winning_formula = lambda difficulty: (int(difficulty) * 3) + 5


def add_score(difficulty):
    new_points = int(points_of_winning_formula(difficulty))
    # print(new_points)
    try:
        score_file = open(SCORES_FILE_NAME, READ_FILE_MODE)
        old_score = score_file.read()
        new_points += int(old_score)
        score_file.close()
    except IOError:
        print(f"{SCORES_FILE_NAME} is missing. File will be created and will contains new game scores: {new_points}")
    except ValueError:
        print(f"{SCORES_FILE_NAME} seems to be empty, {new_points} will be written...")
    except BaseException as e:
        print_exception_error(f"Something went wrong, the following exception occurred: {e.args}")
    finally:
        score_file = open(SCORES_FILE_NAME, WRITE_FILE_MODE)
        score_file.write(str(new_points))
        score_file.close()
