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

        uname_input.clear()
        uname_input.send_keys(self.username)
        passwd_input.clear()
        passwd_input.send_keys(self.password)
        passwd_input.submit()
        time.sleep(2)

        if self.browser.find_elements_by_class_name("_19dFdjzCl1LYGUAL1nstT3")[8].get_attribute("aria-label")\
                == "Déconnexion":
            self.connected = True
        else:
            self.browser.close()
            raise ConnectionError("Could not connect to degiro's website")

    def disconnect(self):
        if self.connected:
            disconnect_button = self.browser.find_elements_by_class_name("_19dFdjzCl1LYGUAL1nstT3")[8]
            disconnect_button.click()
            self.connected = False
            self.browser.close()

    def add_sell_order(self, qty, price1, price2, ordertype, **kwargs):
        # ordertype (1 = limit, 2 = stoploss, 3 = stoplimit)

        # Dealing with optional arguments
        name = kwargs.get('name', None)
        ticker = kwargs.get('ticker', None)

        # Input sanitation (overly paranoid but we're dealing with real money here)
        qty = int(qty)
        price1 = float(price1)
        price2 = float(price2)
        ordertype = int(ordertype)
        if name is None and ticker is None:
            raise ValueError("Name and ticker cannot both be None")
        if qty <= 0:
            raise ValueError("Can't sell less than 1 stock")
        if price1 <= 0:
            raise ValueError("Can't have negative or null sell price")
        if ordertype not in (1, 2, 3):
            raise TypeError("Invalid order type")
        if ordertype == 3 and (price2 <= 0 or price2 < price1):
            raise ValueError("Stop limit price should be smaller than stop loss price.")

        # Handeling the case where we don't have the stock's name
        if name is None:
            name = self.find_ticker_name(ticker)

        # First we cancel all orders for that stock
        # Then we set a new sell order for that stock
        self.cancel_orders(name)


    def find_ticker_name(self, ticker):
        # first searches in database if the ticker already has a name association
        # then checks on degiro's website
        pass

    def cancel_orders(self, name):
        # finds all orders open on a "named" stock and cancels them
        if self.connected:
            # Going to the "Orders" page
            self.browser.get("https://trader.degiro.nl/trader4/#/orders/open")

            # Get all open orders
            orders_delete_btn = self.browser.find_elements_by_xpath("//button[@data-name='orderDeleteButton']")
            orders_delete_btn.get_attribute("title")
