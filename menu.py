#Menu
import finance
import random

def menu_function():
    info = create_account()
    n, s, o, b = info #details of name, surname and occupation are being unpacked
#***************************************************************************************
    #all below will be used by Account to give a summary and balance
    transaction = finance.Transaction()
    budget = finance.Budget()
    finance_tracker = finance.Finance_Tracker(n, s, o)
    budget.create_budget()
#***************************************************************************************
    account = finance.Account(n, s, o) #have to link Account class to the other accounts
    print(f"=====WELCOME {account.n}=====\n")
    menu = """
========= MENU =========

1. Income
2. Expenses
3. Transaction History
4. Exit

========================
"""
    while True:
        try:
            #invalid numeric input continues the program
            option = int(input(f"{menu}\nPlease select option: "))
            if option == 1:
                income_menu = """
========= INCOME MENU =========

1. Add Income
2. Edit Income
3. Delete Income
4. Generate Income Report
===============================
"""
                submenu_income = """
========= INCOME MENU =========

1. Standard Income
2. Subscription
===============================
"""
                income_option = int(input(f"{income_menu}\nPlease select option: "))
                if income_option == 1:
                    sub_income_option = int(input(f"{submenu_income}\nPlease select option: "))
                    if sub_income_option not in (1, 2):
                        raise ValueError("Invalid option")
                    if sub_income_option == 1:
                        transaction.income_transaction(finance_tracker)
                    elif sub_income_option == 2:
                        transaction.subscription_income(finance_tracker)

                elif income_option == 2:
                    transaction.edit_income(finance_tracker)
                elif income_option == 3:
                    transaction.delete_income(finance_tracker)
                elif income_option == 4:
                    transaction.generate_report_income()
                else:
                    print("Invalid option")

            elif option == 2:
                expense_menu = """
========= EXPENSE MENU =========

1. Add Expenses
2. Edit Expenses
3. Delete Expenses
4. Generate Expense Report
===============================
"""
                submenu_expense = """
========= SUB-INCOME MENU =========

1. Standard Expense
2. Subscription
===============================
"""
                expense_option = int(input(f"{expense_menu}\nPlease select option: "))
                if expense_option == 1:
                    sub_expense_option = int(input(f"{submenu_expense}\nPlease select option: "))
                    if sub_expense_option not in (1, 2):
                        raise ValueError("Invalid option")
                    if sub_expense_option == 1:
                        transaction.expense_transaction(finance_tracker, budget)
                    elif sub_expense_option == 2:
                        transaction.subscription_expenses(finance_tracker, budget)

                elif expense_option == 2:
                    transaction.edit_expense(finance_tracker)
                elif expense_option == 3:
                    transaction.delete_expense(finance_tracker)
                elif expense_option == 4:
                    transaction.generate_report_expense()
                else:
                    print("Invalid option")

            elif option == 3:
                transaction.generate_both()
            elif option == 4:
                print("Thank you for using the program...Bye!")
                break
        except ValueError as e:
            print("Error:", str(e))
            raise

def create_account():
    try:
        #Return a tuple then create instance in menu
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        occupation = input("Enter your occupation: ")
        count = 0
        balance = round(random.uniform(0, 100000), 2) #get random value from 0 to 100000 -> random float values rounded off to 2 decimal places

        if name and surname and occupation:
            return (name, surname, occupation)
        while not name or not surname or not occupation:
            count += 1
            if count == 4:
                raise ValueError("Sign up Error! Please contact system administrator for assistance!")

            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            occupation = input("Enter your occupation: ")

        return (name, surname, occupation, balance)
    except ValueError as e:
        print('error:', str(e))
        raise



