# Personal Finance Tracker & Budget Analyzer

A command-line Python application that helps users manage their finances by tracking income, expenses, and budgets.

---

## Features

- Add, edit, and delete income transactions  
- Add, edit, and delete expense transactions  
- Create and manage a budget per category  
- Support for subscription income and expenses  
- Save transaction records to text files (`income.txt`, `expense.txt`)  
- Generate transaction reports  
- User account creation with basic details  

---

## Technologies Used

- Python 3  
- File handling (`.txt` storage)  
- Object-Oriented Programming (OOP)  

---

## Project Structure
```text
Personal-Finance-Tracker/
│
├── main.py # Entry point of the application
├── menu.py # Handles user interaction and menu navigation
├── finance.py # Core logic (transactions, budget, account management)
├── income.txt # Stores income records (generated at runtime)
├── expense.txt # Stores expense records (generated at runtime)
```
---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/tadiwagutuwork-droid/Personal-Finance-Tracker.git
2. Navigate into the project directory:
   ```bash
   cd Personal-Finance-Tracker
3. Run the application:
   ```bash
   python menu.py

---

## Usage

1. Create an account by entering your name, surname, and occupation  
2. Set up your budget categories  
3. Use the menu system to:
   - Add income or expenses  
   - Manage existing transactions  
   - View financial reports  

---

## Budget Categories

- Housing  
- Food  
- Transport  
- Entertainment  
- Health  
- Shopping  
- Subscription (Expenses)  
- Other  

---

## License

This project is licensed under the MIT License.

---

## Author

Tadiwa Gutu  
https://github.com/tadiwagutuwork-droid
