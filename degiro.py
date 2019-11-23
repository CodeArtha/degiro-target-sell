from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tinydb import TinyDB
from tinydb import Query
import time

DATABASE = TinyDB("orders_db.json")

class Degiro:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()
        self.connected = False

    def connect(self):
        self.browser.get("https://trader.degiro.nl/login/#/login")
        time.sleep(2)
        uname_input = self.browser.find_element_by_id("username")
        passwd_input = self.browser.find_element_by_id("password")
        login_button = self.browser.find_element_by_name("loginButtonUniversal")

        uname_input.clear()
        uname_input.send_keys(self.username)
        passwd_input.clear()
        passwd_input.send_keys(self.password)
        login_button.Click()
        time.sleep(2)

        if self.browser.find_element_by_class("_16w6oZfTNqqvo0AKLHs8yK").text == "William Arsac":
            self.connected = True
        else:
            self.browser.Close()
            raise ConnectionError("Could not connect to degiro's website")

    def disconnect(self):
        if self.connected:
            disconnect_button = self.browser.find_element_by_text("Déconnexion")
            disconnect_button.click()
            self.browser.Close()
