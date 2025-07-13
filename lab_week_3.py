"""
Python File that contains all the Tasks from Week 3 lab.
Each task is labeled clearly and separated properly for better understanding.
Topics are mentioned in Week 3 Lab
"""

"""
-------- Section 1: Functions and Scope --------"""


"""Exercise 1"""
# Functions in Python
# A function is a block of code which only runs when it is called

# creating function




def greet_user():
    print("Hello!")
# calling function
greet_user()

print('\n\n')


# function with parameters
def greet_user(name):
    print(f"Hello {name}!")
# calling function
greet_user("John")

print('\n\n')
# functions with more than one parameter
def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")

# calling function
greet_user("John", "Doe")

print('\n\n')

# keyword arguments
greet_user(last_name="Smith", first_name="John")

print('\n\n')


# Default values
def greet_user(first_name, last_name, university="UWS"):
    print(f"Hello {first_name} {last_name} from {university}!")

# calling function
greet_user("John", "Doe")

"""it will also work when we pass the value 
of variable which have default value"""

greet_user("John", "Smith", "UWS London")

print('\n\n')


# Task: Greet each friend in the list
print("Task: Greet each friend in the list\n")

def greet_friends(friend_list):
    for name in friend_list:
        print(f"Hello {name}!")

# Example list of names
friends = ["John", "Jane", "Jack"]

# Calling the function
greet_friends(friends)

print('\n\n')



# Returning values from functions
def add_numbers(num1, num2):
    return num1 + num2

def add_numbers(num1, num2):
    result = num1 + num2
    return result

# calling function
result = add_numbers(5, 3)
print(f"The sum of 5 and 3 is: {result}")

print('\n\n')

# returning multiple values
def add_and_multiply_numbers(num1, num2):
    return num1 + num2, num1 * num2

def add_and_multiply_numbers(num1, num2):
    sum = num1 + num2
    product = num1 * num2
    return sum, product

# calling function and getting multiple values
result_sum, result_product = add_and_multiply_numbers(5, 3)
print(f"The sum of 5 and 3 is: {result_sum}")
print(f"The product of 5 and 3 is: {result_product}")

print('\n\n')



# Task: Calculate Tax Based on Income and Tax Rate
print("Task: Calculate Tax Based on Income and Tax Rate\n")

# Step 1: Define the tax calculation function
def calculate_tax(income, tax_rate):
    tax = income * tax_rate
    return tax

# Step 2: First example with 50,000 and 20% tax rate
result = calculate_tax(50000, 0.2)
print(f"The tax on £50000 at a 20% rate is: £{result}")
print("-" * 40)

# Step 3: Ask the user if they want to calculate more taxes
while True:
    # loop is to do the same thing multiple times
    choice = input("Do you want to calculate more tax? (y/n): ").lower()

    if choice == "y":
        # Take income and tax rate from the user
        income = float(input("Enter the income in £: "))
        tax_rate = float(input("Enter the tax rate (e.g. 0.2 for 20%): "))

        # Step 4: Call the tax calculation function
        # Calculate and print the tax
        tax = calculate_tax(income, tax_rate)
        print(f"The tax on £{income} at a {tax_rate * 100}% rate is: £{tax}")
        print("-" * 40)

    elif choice == "n":
        print("Thank you! Program ended.")
        break

    else:
        print("Invalid input. Please type 'y' or 'n'.")
        
        
print('\n\n')




# Task: Compound Interest Calculator Function
print("Task: Compound Interest Calculator Function\n")

# function have three parameters
def compound_interest(principal, duration, interest_rate):
    # Check if interest_rate is valid
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None

    # Check if duration is valid
    if duration < 0:
        print("Please enter a positive number of years")
        return None

    # Loop through each year and calculate compound interest
    for year in range(1, duration + 1):
        total_for_the_year = principal * (1 + interest_rate) ** year
        print(f"The total amount of money earned by the ",
              "investment in year {year} is {total_for_the_year:.2f} £")

    # Return final value as an integer
    final_value = principal * (1 + interest_rate) ** duration
    return int(final_value)

# Example test
final_result = compound_interest(1000, 5, 0.03)
print(f"\nFinal investment value after 5 years: {final_result:.2f} £")
print("-" * 40)
print('Using Assertions')
assert compound_interest(1000, 5, 0.03) == 1159



print('\n\n')


"""Exercise 2"""
# Variable Scope

def new_function():
    my_new_variable = 5

new_function() # call the function. No problems here.
"""
this will cause an error because this variable is 
defined inside the function and can only be 
accessed and used inside the function
"""
# print(my_new_variable) 

"""variables defined outside the function 
can be accessed inside the function too """

def new_function():
    my_new_variable = 5
    print(my_new_variable)

new_function()

print('\n\n')


""" 
-------- Section 2: Assertions and Errors --------
"""

"""Exercise 6"""
# Assertions
# Example test for compound interest function that was in section 1 Task
assert compound_interest(1000, 5, 0.03) == 1159 

print('\n\n')

"""Exercise 7"""
# Identifying and Fixing Common Errors 

# Task 5: Fixing Errors
print("Task 5: Fixing Errors\n")


# Syntax Error
# pritn("Hello, World!")  

# Corrected Code
print("Hello, World!")

print('\n\n')


# Name Error: 
my_name = "Alice" 
# print("Hello, " + myname) 

# Corrected Code:
# define the variable correctly and then using it
favorite_color = "Blue"  
print("My favorite color is", favorite_color)

print('\n\n')


# Value Error: 
# number1 = "5" 
# number2 = 3 
# result = number1 + number2 

# Corrected Code:
# Convert the string to an integer then perform the operation
number1 = int("5")  
number2 = 3  
result = number1 + number2
print("The sum of", number1, "and", number2, "is", result)



print('\n\n')

# Index Error
fruits = ["apple", "banana", "orange"] 
# print(fruits[3])


# Corrected Code:
# Use a valid index for the list
# Index starts from 0, thats why end at 1 less then the length of the list
fruits = ["apple", "banana", "orange"] 
print('Fruit at the index 2 is', fruits[2])


print('\n\n')

# Indentation Error
# if 5 > 2: 
# print("Five is greater than two!") 

# Corrected Code:
# Indentation is correct
if 5 > 2:
    print("Five is greater than two!")


print('\n\n')
