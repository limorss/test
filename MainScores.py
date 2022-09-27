"""
    Student Name: Limor Segal Shevah
    Project: World Of Games
"""
from flask import Flask
from Utils import SCORES_FILE_NAME, READ_FILE_MODE
from Utils import BAD_RETURN_CODE


invalid_score_text = lambda error: f"<h1><div id=\"score\" style=\"color:red\">{error}</div></h1>"
valid_score_text = lambda score: f"<h1>The score is <div id=\"score\">{score}</div></h1>"


# Create http server and run it
app = Flask("Scores Game")


@app.route('/')
def score_server():
    text_to_display = ''
    try:
        score_file = open(SCORES_FILE_NAME, READ_FILE_MODE)
        score = score_file.read()
        score_file.close()
        if '' == score:
            raise IOError(f"Something went wrong... {SCORES_FILE_NAME} is empty!")
        if not score.isnumeric():
            raise IOError(f"Something was corrupted... {SCORES_FILE_NAME} has non numeric value: {score}")
        text_to_display = valid_score_text(score)
    except IOError as e:
        text_to_display = invalid_score_text(f"Bad return code ({str(BAD_RETURN_CODE)}) when opening {SCORES_FILE_NAME},"
                                             f" {e.strerror}")
    finally:
        return f"<html><head><title>Scores Game</title></head><body>{text_to_display}</body></html>"


app.run(host="0.0.0.0", port=5000, debug=False)
