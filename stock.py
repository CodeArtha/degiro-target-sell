import sys
import os
from tinydb import TinyDB
from tinydb import Query

# columns = order id | ticker | qty | target | status (executed) | tradingview
# DATABASE.insert({'ticker': None,
#                  'qty': None,
#                  'target': None,
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
    tgt = float(input("Target Sell Price: "))
    order = {'ticker': ticker,
             'qty': amount,
             'target': tgt,
             'type': order_type,
             'status': "open",
             'URL': None}
    DATABASE.insert(order)

    input("Press ENTER to go back to main menu")
    menu_actions['main_menu']()
    return None


def edit_order():
    clear_terminal()
    ticker = input("Ticker of the order to edit: ").upper()

    print("Fetching current orders on {}...".format(ticker))
    order = Query()
    for result in DATABASE.search((order.ticker == ticker) & (order.status == "open")):
        print(result.doc_id, " : ", result)

    order_id = int(input("Order ID you want to edit: "))

    # order_type = DATABASE.get(doc_id=order_id)["type"]

    tgt = float(input("New TARGET price: "))

    # change order price
    DATABASE.update({"target": tgt}, doc_ids=[order_id])
    # print new order
    input("Press ENTER to go back to main menu")
    menu_actions['main_menu']()
    return None


def view_open_orders():
    order = Query()
    for result in DATABASE.search(order.status == "open"):
        print(result.doc_id, " ", result)
    input("Press ENTER to go back to main menu")
    menu_actions['main_menu']()
    return None


def cancel_order():
    print("Retrieving all open orders...")
    view_open_orders("open")

    order_id = int(input("\nOrder ID to cancel: "))
    DATABASE.update({"status": "cancelled"}, doc_ids=[order_id])

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


# =======================
#    MENUS DEFINITIONS
# =======================
menu_actions = {
    'main_menu': main_menu,
    '1': add_order,
    '2': view_open_orders,
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


