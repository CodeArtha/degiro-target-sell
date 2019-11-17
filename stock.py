import sys
import os
from tinydb import TinyDB, Query

# columns = order id | ticker | qty | price1 | price2 | direction (B, S) |
#           type (1 = limit, 2 = stoploss, 3 = stoplimit) |
#           status (open, executed, cancelled) | tradingview
# DATABASE.insert({'ticker': None,
#                  'qty': None,
#                  'price1': None,
#                  'price2': None,
#                  'direction': None,
#                  'type': None,
#                  'status': None,
#                  'URL': None})
DATABASE = TinyDB("orders_db.json")


def clear_terminal():
    # Clears the current terminal OS independant
    os.system('cls' if os.name == 'nt' else 'clear')
    return None


def main_menu():
    clear_terminal()
    print("Welcome,")
    print("Please choose an action:\n")
    print("1. Add a target order on a ticker")
    print("2. List open orders")
    print("3. Edit the order set on a ticker")
    print("4. Cancel an order")
    print("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return None


def add_order():
    clear_terminal()
    print("Registering a new order.\n")

    ticker = input("Ticker: ").upper()
    amount = int(input("Amount: "))
    direction = input("Order direction (B)uy/(S)ell: ").upper()

    if direction not in ("B", "S"):
        print("Direction has to be B or S")

    print("Order type: ")
    print("1. Limit")
    print("2. Stop Loss")
    print("3. Stop Limit")
    type = int(input(" >>  "))

    if type == 3:
        price1 = float(input("Stop Loss price: "))
        price2 = float(input("Stop Limit price: "))
    else:
        price1 = float(input("Stop Loss price: "))
        price2 = None

    order = {'ticker': ticker,
             'qty': amount,
             'price1': price1,
             'price2': price2,
             'type': type,
             'status': "open",
             'URL': None}
    DATABASE.insert(order)

    input("Press ENTER to go back to main menu")
    menu_actions['main_menu']()
    return None


def edit_order():
    clear_terminal()
    ticker = input("Ticker of the order to edit: ")
    # print all orders open for that ticker
    order_id = input("Order ID: ")
    price = input("New price: ")
    # change order price
    DATABASE.insert({})
    # print new order
    input("Press ENTER to go back to main menu")
    menu_actions['main_menu']()
    return None


def view_orders():
    # read all orders from database where status = open
    input("Press ENTER to go back to main menu")
    menu_actions['main_menu']()
    return None


def cancel_order():
    input("Order ID: ")
    # mark order status as cancelled
    print("Order cancelled")
    input("Press ENTER to go back to main menu")
    menu_actions['main_menu']()
    return None


def exec_menu(choice):
    clear_terminal()
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return None


# Back to main menu
def back():
    menu_actions['main_menu']()
    return None


# Exit program
def exxit():
    sys.exit()
    return None


# =======================
#    MENUS DEFINITIONS
# =======================
menu_actions = {
    'main_menu': main_menu,
    '1': add_order,
    '2': view_orders,
    '3': edit_order,
    '4': cancel_order,
    '9': back,
    '0': exxit,
}


# =======================
#      MAIN PROGRAM
# =======================
if __name__ == "__main__":
    # Launch main menu
    main_menu()


