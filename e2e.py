"""
    Student Name: Limor Segal Shevah
    Project: World Of Games
"""
import shutil

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import argparse
import os
from Utils import MAX_SCORE, SUCCESS_RETURN_CODE, BAD_RETURN_CODE

DEFAULT_FLASK_APP_URL = "http://127.0.0.1:5000/"
BIN_CHROME_DRIVER_DEST = "/usr/local/bin"


def test_scores_service(url):
    try:
        paths = []
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        full_bin_path = ChromeDriverManager(path=BIN_CHROME_DRIVER_DEST).install()
        my_driver = webdriver.Chrome(service=ChromeService(full_bin_path), chrome_options=chrome_options)
        my_driver.get(url)
        score = my_driver.find_element(by="xpath", value='//*[@id="score"]').text
        print(score)
        my_driver.close()
        return int(score) in range(1, MAX_SCORE + 1)
    except ValueError as e:
        print(e)
        return False


def main_function(url):
    if test_scores_service(url):
        retun SUCCESS_RETURN_CODE
    else:
        print("Score is not in range...")
        return BAD_RETURN_CODE


parser = argparse.ArgumentParser(description='End to end testing',
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-u', action='store', dest='flask_url', default=DEFAULT_FLASK_APP_URL, type=str,
                    help=f"Flask server url e.g. {DEFAULT_FLASK_APP_URL}")
args = parser.parse_args()
flask_url = args.flask_url
if main_function(flask_url) < 0:
    exit(1)
