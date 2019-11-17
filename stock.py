import sys
import os


def clear_terminal():
    # Clears the current terminal OS independant
    os.system('cls' if os.name == 'nt' else 'clear')


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
    return


def add_order():
    clear_terminal()
    print("Registering a new order.")
    print("Currently only stop loss orders.\n")
    ticker = input("Ticker: ")
    amount = input("Amount: ")
    direction = input("Buy or Sell: ")
    price = input("Stop Loss price: ")

    # Todo
    # Sanitize user input
    # Add order to database
    # Print complete order
    input("Press ENTER to go back to main menu")
    menu_actions['main_menu']()
    return 1


def edit_order():
    clear_terminal()
    ticker = input("Ticker of the order to edit: ")
    # print all orders open for that ticker
    order_id = input("Order ID: ")
    price = input("New price: ")
    # change order price
    # save new order to database
    # print new order
    input("Press ENTER to go back to main menu")
    menu_actions['main_menu']()
    return 1


def view_orders():
    # read all orders from database where status = open
    input("Press ENTER to go back to main menu")
    menu_actions['main_menu']()
    return 1


def cancel_order():
    input("Order ID: ")
    # mark order status as cancelled
    print("Order cancelled")
    input("Press ENTER to go back to main menu")
    menu_actions['main_menu']()
    return 1


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
    return


# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exxit():
    sys.exit()


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


