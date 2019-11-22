from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TradingView:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()

    # connect with username and password
    def connect(self):
        # Going to the home page and clicking the signin button
        self.browser.get("https://tradingview.com#signin")
        time.sleep(3)

        # Find the input fields of the signin form
        uname_input = self.browser.find_element_by_name("username")
        passwd_input = self.browser.find_element_by_name("password")

        # Filling in the form
        uname_input.clear()
        uname_input.send_keys(self.username)
        passwd_input.clear()
        passwd_input.send_keys(self.password)
        # had to submit from the password field as I couldn't find a unique
        # identifier for the form's submit button.
        passwd_input.submit()
        time.sleep(3)


