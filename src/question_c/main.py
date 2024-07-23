#add import

from question_c import stock_purchase_history

def display_stock_purchase_history():
    while True:
        print("Welcome to your Stock Portfolio, please read carefully as the following menu has changed:")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            stock_purchase_history()
        elif choice == '2':
            print("Exiting... Have good day!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

display_stock_purchase_history()