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

