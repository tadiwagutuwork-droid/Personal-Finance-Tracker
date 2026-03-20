#Personal Finance Tracker & Budget Analyzer
import random
from datetime import date

class Transaction: #saves it to the text files, dictionaries of transactions
    def __init__(self):
        self.transaction_history = {}
        self.transaction_id = []

    def income_transaction(self, finance_tracker): #finance_tracker is an instance of Finance_Tracker to access the balance variable
        #{id: {date, amount, category}}
        try:
            info = self.get_info() #return a tuple
            category = info[0]
            t_date = info[1]
            t_id = self.generate_id()
            t_amount = float(input("Enter income amount: "))
            if t_amount <= 0:
                raise ValueError("No negative amounts!")
            t_category = input(f"{category[0]}\nEnter category: ")

            self.transaction_history.update({t_id: {"date": t_date, "amount": t_amount, "category": t_category}})
            self.record_income(t_id) #write to a file
            finance_tracker.balance += t_amount #update balance
            print("Income Created Successfully!\n")
        except ValueError as e:
            print("Error:",  str(e))

    def expense_transaction(self, finance_tracker, budget_instance): #finance_tracker is an instance of Finance_Tracker to access the balance variable
        try:
            info = self.get_info() #return a tuple
            category = info[0]
            t_date = info[1]
            t_id = self.generate_id()
            t_amount = float(input("Enter expense amount: "))
            if t_amount < 0:
                raise ValueError("No negative amounts!")
            elif t_amount > finance_tracker.balance:
                raise ValueError("Exceeding balance!")
            t_category = input(f"{category[1]}\nEnter category: ")
            t_category = t_category.capitalize()

            if budget_instance.budget[t_category]['limit'] > t_amount:
                print("Going Over The Budget!\n")
            elif (t_amount * 0.8) <= budget_instance.budget[t_category]['limit'] <= t_amount: #approaching budget
                print('Nearing Budget\n')
            elif (t_amount * 0.8) > budget_instance.budget[t_category]['limit']:
                print("Budget Going Well!\n")
            budget_instance.budget[t_category]['spent'] = t_amount
            budget_instance.budget_balance -= t_amount

            self.transaction_history.update({t_id: {"date": t_date, "amount": t_amount, "category": t_category}})
            self.record_expenses(t_id) #write to a file
            finance_tracker.balance -= t_amount #update balance
            print("Expense Created Successfully!\n")

        except (ValueError, KeyError) as e:
            print("Error:",  str(e))

    def record_income(self, t_id):
        try:
            with open('income.txt', 'a') as file:
                #({t_id: {"date": t_date, "amount": t_amount, "category": t_category}})
                file.write(f"{(self.transaction_history["date"])} | {self.transaction_history[t_id]} | {self.transaction_history["category"]} | R{self.transaction_history["amount"]:,.2f}\n")
                print("Recorded Successfully!\n")

        except FileNotFoundError as e:
            print("Error", str(e))

    def record_expenses(self, t_id):
        try:
            with open('expense.txt', 'a') as file:
                #({t_id: {"date": t_date, "amount": t_amount, "category": t_category}})
                file.write(f"{(self.transaction_history["date"])} | {self.transaction_history[t_id]} | {self.transaction_history["category"]} | R{self.transaction_history["amount"]:,.2f}\n")
                print("Recorded Successfully!\n")
        except FileNotFoundError as e:
            print("Error", str(e))

    def subscription_expenses(self, finance_tracker, budget_instance):
        t_id = f"SUB{random.randint(0, 9)}{random.randint(0, 9)}E" #e.g. SUB45E
        try:
            t_id = str(t_id) #Maybe ValueError would be raised
            amount = input("Enter subscription amount: ")
            if amount < 0:
                raise ValueError("No negative amounts!")
            elif amount > finance_tracker.balance:
                raise ValueError("Exceeding balance!")
            category = 'Subscription (Expenses)'
            info = self.get_info()
            t_date = info[1]
            if not self.transaction_id: #if list is empty
                self.transaction_id.append(t_id) #add to list
                return t_id
            while t_id in self.transaction_id: #if the same transaction ID is present in the list
                t_id = f"SUB{random.randint(0, 9)}{random.randint(0, 9)}E"

            if budget_instance.budget[category]['limit'] > amount:
                print("Going Over The Budget!\n")
            elif (amount * 0.8) <= budget_instance.budget[category]['limit'] <= amount: #approaching budget
                print('Nearing Budget\n')
            elif (amount * 0.8) > budget_instance.budget[category]['limit']:
                print("Budget Going Well!\n")
            budget_instance.budget[category]['spent'] = amount
            budget_instance.budget_balance -= amount

            self.transaction_id.append(t_id) #add to list
            self.transaction_history.update({t_id: {"date": t_date, "amount": amount, "category": category}})
            finance_tracker.balance -= amount #update balance
            print("Subscription Created Successfully!")
        except ValueError as e:
            print("Error:", str(e))

    def subscription_income(self, finance_tracker):
        #add a subscription based income
        t_id = f"SUB{random.randint(0, 9)}{random.randint(0, 9)}I" #e.g. SUB78I
        try:
            t_id = str(t_id) #Maybe ValueError would be raised
            amount = input("Enter subscription amount: ")
            category = 'Subscription (Income)'
            info = self.get_info()
            t_date = info[1]
            if not self.transaction_id: #if list is empty
                self.transaction_id.append(t_id) #add to list
                return t_id
            while t_id in self.transaction_id: #if the same transaction ID is present in the list
                t_id = f"SUB{random.randint(0, 9)}{random.randint(0, 9)}I"

            self.transaction_id.append(t_id) #add to list
            self.transaction_history.update({t_id: {"date": t_date, "amount": amount, "category": category}})
            self.record_income(t_id) #write to a file
            finance_tracker.balance += amount #update balance
            print("Subscription Created Successfully!")

        except ValueError as e:
            print("Error:", str(e))

    def generate_id(self): #create ID
        t_id = f"{chr(random.randint(65, 90))}{random.randint(0, 9)}{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}{random.randint(0, 9)}{random.randint(0, 9)}" #e.g. H7ZN96
        try:
            t_id = str(t_id) #Maybe ValueError would be raised
            if not self.transaction_id: #if list is empty
                self.transaction_id.append(t_id) #add to list
                return t_id
            while t_id in self.transaction_id: #if the same transaction ID is present in the list
                t_id = f"{chr(random.randint(65, 90))}{random.randint(0, 9)}{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}{random.randint(0, 9)}{random.randint(0, 9)}"

            self.transaction_id.append(t_id) #add to list
            return t_id
        except ValueError as e:
            print("Error:", str(e))

    def get_info(self):
        categories = (
        (
    "1. Salary",
    "2. Business",
    "3. Investment",
    "4. Other"
),(
    "1. Housing",
    "2. Food",
    "3. Transport",
    "4. Entertainment",
    "5. Health",
    "6. Shopping",
    "7. Other"
)
)
        while True:
            day = random.randint(1, 31)
            month = random.randint(1, 12)
            year = 2026

            if 1<=day<=31 and month in (1, 3 ,5 , 7, 8, 10, 12):
                t_date = date(year, month, day)
                break
            elif 1<=day<=30 and month in (4, 6, 9, 11):
                t_date = date(year, month, day)
                break
            elif 1<=day<=28 and month == 2:
                if year%4==0:
                    t_date = date(year, month, day)
                    break
                elif year%4!=0:
                    t_date = date(year, month, day)
                    break

        return (categories, t_date)

    def delete_income(self, finance_tracker): #remember to update balance
        try:
            t_id = input("Enter valid transaction ID: ")
            t_id = t_id.upper()
            count = 3
            while t_id not in self.transaction_id or count !=0:
                count -= 1
                t_id = input("Re-enter valid transaction ID: ")
                if count == 0:
                    raise ValueError("Transaction ID does not exist!")

            finance_tracker.balance -= self.transaction_history[t_id["amount"]]
            self.transaction_history.pop(t_id)
            print("Deleted Successfully!\n")
        except (KeyError, ValueError) as e:
            print("Error:", str(e))

    def delete_expense(self, finance_tracker, budget_instance): #remember to update balance
        try:
            t_id = input("Enter valid transaction ID: ")
            t_id = t_id.upper()
            count = 3
            while t_id not in self.transaction_id or count !=0:
                count -= 1
                t_id = input("Re-enter valid transaction ID: ")
                if count == 0:
                    raise ValueError("Transaction ID does not exist!")

            category = self.transaction_history[t_id["category"]]
            finance_tracker.balance += self.transaction_history[t_id["amount"]]
            budget_instance.budget_balance += self.transaction_history[t_id["amount"]]
            budget_instance.budget[category]['spent'] -= self.transaction_history[t_id["amount"]]
            self.transaction_history.pop(t_id)
            print("Deleted Successfully!\n")
        except (KeyError, ValueError) as e:
            print("Error:", str(e))

    def edit_income(self, finance_tracker): #remember to update balance
        try:
            t_id = input("Enter valid transaction ID: ")
            t_id = t_id.upper()
            count = 3
            while t_id not in self.transaction_id or count !=0:
                count -= 1
                t_id = input("Re-enter valid transaction ID: ")
                if count == 0:
                    raise ValueError("Transaction ID does not exist!")

            self.transaction_history.pop(t_id)
            self.income_transaction(finance_tracker)
            print("Edited Successfully!\n")
        except (KeyError, ValueError) as e:
            print("Error:", str(e))

    def edit_expense(self, finance_tracker): #remember to update balance
        try:
            t_id = input("Enter valid transaction ID: ")
            t_id = t_id.upper()
            count = 3
            while t_id not in self.transaction_id or count !=0:
                count -= 1
                t_id = input("Re-enter valid transaction ID: ")
                if count == 0:
                    raise ValueError("Transaction ID does not exist!")

            self.transaction_history.pop(t_id)
            self.expense_transaction(finance_tracker)
            print("Edited Successfully!\n")
        except (KeyError, ValueError) as e:
            print("Error:", str(e))

    def generate_report_income(self):
        try:
            with open("income.txt", "r") as file:
                print(file.read())
        except FileNotFoundError as e:
            print("Error:", str(e))

    def generate_report_expense(self):
        try:
            with open("expense.txt", "r") as file:
                print(file.read())
        except FileNotFoundError as e:
            print("Error:", str(e))

    def generate_both(self):
        try:
            income = ''
            expense = ''
            with open("income.txt", "r") as file:
                income = file.read()
            with open('expense.txt', 'r') as file:
                expense = file.read()
            with open("transaction_report.txt", "a") as file:
                file.write(f"====== TRANSACTION HISTORY ====== \n{income}\n{expense}n")

        except FileNotFoundError as e:
            print("Error:", str(e))

class Budget: #create budget, access to balance
    def __init__(self):
        self.budget = {} #initialize with empty dictionary - {category: {limit, spent}}
        self.budget_balance = 0

    def create_budget(self):
        try:
            categories = ("Housing", "Food", "Transport", "Entertainment", "Health", "Shopping", "Subscription (Expenses)", "Other")
            spent = 0 #default value
            for category in categories:
                limit = float(input(f"==== {category} ====\nEnter limit: "))
                if limit < 0:
                    raise ValueError("No negative values allowed")
                self.budget_balance += limit
                self.budget.update({category: {'limit': limit, 'spent': spent}})
            print("Budget Created Successfully!\n")

        except (ValueError, TypeError) as e:
            print("Error:", str(e))

    def __str__(self):
        return f"Budget Balance: R{self.budget_balance:,.2f}"

class Finance_Tracker: #balance is stored here
    def __init__(self, balance = 0):
        self.balance = balance #initial balance

    def __str__(self):
        return f"Balance: R{self.balance:,.2f}"
class Account:
    def __init__(self, name, surname, occupation):
        self.name = name
        self.surname = surname
        self.occupation = occupation

    def __str__(self):
        header = "======== ACCOUNT DETAILS ========"
        end = '=' * len(header)
        return f"{header}\nName: {self.name} {self.surname}\nOccupation: {self.occupation}\n{end}"

#The instances of Finance_Tracker will be managed by Account
#Remember the Student, Teacher and Principal classes example