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
CHROME_DRIVER_BIN = "chromedriver"

def recursive_find(filename, paths, src):
    if os.path.isdir(src):
        for item in os.listdir(src):
            src_item = f"{src}{os.sep}{item}"
            if os.path.isfile(src_item) and (item == filename):
                paths.append(src_item)
            elif os.path.isdir(src_item):
                new_dest = os.path.join(src, item)
                recursive_find(filename, paths, new_dest)


def test_scores_service(url):
    try:
        paths = []
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        x = ChromeDriverManager(path=BIN_CHROME_DRIVER_DEST).install()
     #   recursive_find(CHROME_DRIVER_BIN, paths, BIN_CHROME_DRIVER_DEST)
     #   print(f"Copying {paths[0]} to {BIN_CHROME_DRIVER_DEST}")
     #   shutil.copy(paths[0], f"{BIN_CHROME_DRIVER_DEST}{os.sep}{CHROME_DRIVER_BIN}")
        my_driver = webdriver.Chrome(service=ChromeService(x), chrome_options=chrome_options)
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
        return SUCCESS_RETURN_CODE
    else:
        return BAD_RETURN_CODE


parser = argparse.ArgumentParser(description='End to end testing',
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-u', action='store', dest='flask_url', default=DEFAULT_FLASK_APP_URL, type=str,
                    help='Flask server url e.g. http://127.0.0.1:5000/')
args = parser.parse_args()
flask_url = args.flask_url
main_function(flask_url)
