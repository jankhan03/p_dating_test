from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

user_sessions = {}


class UserSession:
    # def __init__(self):
    #     chrome_options = webdriver.ChromeOptions()
    #     service = Service(executable_path=os.environ.get("CHROMEDRIVER_PATH"))
    #     chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    #     chrome_options.add_argument("--headless")
    #     chrome_options.add_argument("--disable-dev-shm-usage")
    #     chrome_options.add_argument("--no-sandbox")
    #     chrome_options.add_argument("--window-size=1280,800")
    #
    #     self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()

        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1280,800")

        self.driver = webdriver.Chrome(options=chrome_options)

    def close(self):
        self.driver.quit()


def get_user_session(user_id):
    if user_id not in user_sessions:
        user_sessions[user_id] = UserSession()
    return user_sessions[user_id]
