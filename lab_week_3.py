"""
Python File that contains all the Tasks from Week 3 lab.
Each task is labeled clearly and separated properly for better understanding.
"""


# Task 1: Greet each friend in the list

print("="*40)
print("Task 1: Greet each friend in the list\n")

def greet_friends(friend_list):
    for name in friend_list:
        print(f"Hello {name}!")

# Example list of names
friends = ["John", "Jane", "Jack"]

# Calling the function
greet_friends(friends)

print("="*40)


# Task 2: Calculate Tax Based on Income and Tax Rate
print("Task 2: Calculate Tax Based on Income and Tax Rate\n")

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
    choice = input("Do you want to calculate more tax? (y/n): ").lower()

    if choice == "y":
        # Take income and tax rate from the user
        income = float(input("Enter the income in £: "))
        tax_rate = float(input("Enter the tax rate (e.g. 0.2 for 20%): "))

        # Calculate and print the tax
        tax = calculate_tax(income, tax_rate)
        print(f"The tax on £{income} at a {tax_rate * 100}% rate is: £{tax}")
        print("-" * 40)

    elif choice == "n":
        print("Thank you! Program ended.")
        break

    else:
        print("Invalid input. Please type 'y' or 'n'.")
        
        
print("="*40)




# Task 3: Compound Interest Calculator Function
print("Task 3: Compound Interest Calculator Function\n")

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
        print(f"The total amount of money earned by the investment in year {year} is {total_for_the_year:.2f} £")

    # Return final value as an integer
    final_value = principal * (1 + interest_rate) ** duration
    return int(final_value)

# Example test
final_result = compound_interest(1000, 5, 0.03)
print(f"\nFinal investment value after 5 years: {final_result:.2f} £")
# assert compound_interest(1000, 5, 0.03) == 1159



print("="*40)


# Task 4: Variable Scope

# Task 5: Fixing Errors
print("Task 5: Fixing Errors\n")


# Syntax Error
print("Syntax Error")
print("Wrong Code: print('Hello, World!')")
# pritn("Hello, World!")  

# Corrected Code
print("Correct Code")
print("print('Hello, World!')")

print("-"*40)

# Name Error: 
print("Name Error")
print("Wrong Code: print('My favorite color is', favorite_color)")
# print("My favorite color is", favorite_color) 

# Corrected Code:

# Define the variable before using it
print('Define the Variable before using it \nfavorite_color = "Blue" \nprint("My favorite color is", favorite_color)')

# favorite_color = "Blue"  
# print("My favorite color is", favorite_color)



# Value Error: 
# number1 = "5" 
# number2 = 3 
# result = number1 + number2 

# Corrected Code:
# Convert the string to an integer
number1 = int("5")  
number2 = 3  
result = number1 + number2






