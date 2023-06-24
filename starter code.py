"""This program emulates a simple expense tracking program. It employs various functions
to add expenses to a list, save those expenses, and perform a certain number of 
operations on those expenses (total cost, matching of categories, etc.)

Task: Your task is to complete the implementation of the code and make sure that matches
the requirements set in the assignment's prompt.
First, you will have to make your code identifiable by setting the following information.

******************************************************
Name: <ISIMBI Aimable Cherif>
Andrew ID: <icherif
Semester: Summer 2023
Course: Introduction to Python
Last modified: <24th June 2023; 12:24>
******************************************************

"""

from typing import Tuple

## Declare a global variable to contain all the expenses processed in the program
expenses = []


class BadInputException(Exception):
   """Vanilla exception class used for testing"""
   pass

def add_expense(category: str, amount: float):

   global expenses
   

   # Verify that the category variable contains at least three characters
   if len(category) < 3:
      raise BadInputException("Invalid input: Category should contain at least three characters")
   
    # Verify that the amount variable is a floating value strictly greater than zero
   try:
      amount = float(amount)
      if amount <= 0:
         raise BadInputException("Invalid input: Amount should be a positive number")
   except ValueError:
      raise BadInputException("Invalid input: Amount should be a valid number")   
   
   # Now that you have confirmed that the values are valid, you can add them to the list
   expenses.append((category, amount))


def dump_expenses(file_path = 'expenses.txt'):
   """Dumps the content of the list to a file

      Returns: None

      Args:
         - file_path: the location of the output file. type 'string'
   """
   global expenses
   # Open the file by overriding its content first (https://docs.python.org/3/tutorial/inputoutput.html#tut-files)

   with open(file_path, 'w') as file:

      #For each tuple in the `expenses`' list, write a line in the file in the CSV format (e.g., Clothes,10.05)
      for category, amount in expenses:
         file.write(f'{category},{amount:.2f}\n')
   
def read_expenses(file_path = 'expenses.txt'):
   """Reads the expenses from a file and saves it as a tuple into the expenses list

   Returns: None

   Args:
      - file_path: the path to the input file. type: string
   """
   global expenses
   
   try:
      with open(file_path, 'r') as file:
         for line in file:
            line = line.strip()
            if line:
               try:
                  category, amount = line.split(',')
                  amount = float(amount)
                  expenses.append((category, amount))
               except ValueError:
                  print(f"Invalid line: {line}. Skipping...")   
   except FileNotFoundError:
      # If the file does not exist, safely return from the function.
      return               


def get_expenses_by_category(category):
   """Returns a list of all the expenses that matches the category passed as argument.

   Args:
      - category: the category to match the expenses against.

   Returns:
      A list of expenses matching the set criteria
   """
   global expenses

   #Return a list of tuple of expenses of which the category is equal to the parameter
   return [(c,a) for c, a in expenses if c == category]

def calculate_total_expenses():
   """Returns the total of the amounts recorded as expenses.

   Args: None

   Returns: the total amount of the expenses

   """
   global expenses
   #compute and return the total of the amounts in the list.

   return sum(amount for _, amount in expenses)

def get_menu_action() -> int:
   """This function shows the menu and interprets the action to be done
   by the user.

   Args: None
   Returns: the user's selection.

   """
   #Change the loop's condition so that the user keeps being prompted
   # until their input is valid (i.e. in [1, 4])
   while True:
      print('Menu:')
      print('1. Add an expense')
      print('2. View expenses by category')
      print('3. Calculate total expenses')
      print('4. Exit')

      try:
         #Modify the next line to have the `choice` variable store the selectionof the user
         choice = int(input('Enter your choice: ')) 
         if choice in range(1, 5):
            return choice
         else:
            print('Invalid choice. Please try again.')
      except ValueError:
         print('Invalid input. Please enter a valid number.')      

def print_expense(expense: Tuple[str, float]) -> str:
   """Prints an instance of an expense.

   Args:
      - expense: the expense to be displayed. type: a tuple of a string and a floating point number

   Returns:
      - The string representation to be displayed
   """
   #Produce an output such that the line starts with a | and ends with the same |.
   # the category should be output by using 10 characters, left-aligned, space-filled.
   # the amount is preceded by a $ sign, and occupies as well 10 characters, left-aligned, space filled.
   # here space filled means that if there is less than 10 characters, you should fill the
   # line with spaces. Extra characters can be truncated. Use 2 decimal positions for the amount.
   
   category, amount = expense
   return f'|{category:<10}|${amount:<10.2f}|'

if __name__ == "__main__":
   #read the expenses, if file exists, into the 'expenses' list
   read_expenses()

   # Retrieve the user's choice
   while True:
      command = get_menu_action()
      if command == 1:
         category = input('Expense Category: ')
         amount = input('Expense Amount: ')
         try:
            add_expense(category=category, amount=amount)
         except BadInputException:
            print('Invalid value!')
      elif command == 2: 
         category = input('Expense Category: ')
         expenses = get_expenses_by_category(category=category)
         print('|Category  |Amount    |')
         print('***********************')
         for expense in expenses:
            print(expense)

      elif command == 3:
         total = calculate_total_expenses()
         print(f'Total expenses is: {total:.2f}')
      elif command == 4:
         # Save the list of expenses into a file for future use
         dump_expenses()
         print('Expenses saved. Exiting...')

         #change the next statement to exit the program gracefully
         break
      else:
         raise ValueError('Invalid command entered')