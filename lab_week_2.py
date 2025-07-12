"""
Python File that contains all the Tasks from Week 2 lab.
Each task is labeled clearly and separated properly for better understanding.
"""


print('\n\n\n')

"""

-------- Section 1: Comparisons and Conditionals --------

"""

"""Exercise 1"""
# Comparison Operators

# example 1
is_true = False
print("is_true:", is_true)

# example 2
is_true = 5 > 4
print("5 > 4:", is_true)

# example 3
a = 5
b = 10

print(a == b)   # False
print(a != b)   # True
print(a <= b)   # True
print(a >= b)   # False



print('\n\n')

"""Exercise 2"""
# Logical Operators

# example 1
age = 25
is_in_age_range = age > 20 and age < 30

print("is_in_age_range:", is_in_age_range)

# example 2
x = 5
y = 10

print(x > 0 and y > 0)    # True
print(x > 0 or y < 0)     # True
print(not(x > 0))         # False


print('\n\n')

"""Exercise 3"""
# If Conditionals
# example 1
age = 19
age_group = "child"
if age > 18:
    age_group = "adult"
    print(f"The age group is {age_group}")

# example 2
age = 13
age_group = "child"
if age > 18:
    age_group = "adult"
    print(f"The age group is {age_group}")


print('\n\n')

"""Exercise 4"""
# If-else Conditionals

# example 1
wind_speed = 30
if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")
    
# example 2
wind_speed = 5
if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")

print('\n\n')


"""Exercise 5"""
# If-elif-else Conditionals

# example 1
grade = 55
if grade < 50:
    print("You failed")
elif grade < 60:
    print("You passed")
elif grade < 70:
    print("You got a good pass")
else:
    print("You got an excellent pass")

# example 2
grade = 40
if grade < 50:
    print("You failed")
elif grade < 60:
    print("You passed")
elif grade < 70:
    print("You got a good pass")
else:
    print("You got an excellent pass")

# example 3
grade = 65
if grade < 50:
    print("You failed")
elif grade < 60:
    print("You passed")
elif grade < 70:
    print("You got a good pass")
else:
    print("You got an excellent pass")

# example 4
grade = 80
if grade < 50:
    print("You failed")
elif grade < 60:
    print("You passed")
elif grade < 70:
    print("You got a good pass")
else:
    print("You got an excellent pass")
    

print('\n\n')


"""Exercise 6"""

# Task: Compare Temperatures
print("Task: Compare Temperatures\n")

# Just setting two temperature values
temperature1 = 25
temperature2 = 30

# Showing what values we’re comparing
print(f"Temperature 1: {temperature1}°C")
print(f"Temperature 2: {temperature2}°C")

# Checking if both are the same or different
if temperature1 == temperature2:
    print("Result: Both temperatures are the same.")
else:
    print("Result: The temperatures are different.")

print('\n\n')


""" 

-------- Section 2: Python Lists --------

"""

"""Exercise 1"""
# Creating a List
integer_list = [1, 2, 3, 4, 5]

# list of strings
string_list = ["apple", "banana", "orange", "grape"]

# empty list
empty_list = []

# list with different data types
list_with_different_types = [1, "two", 3.0, True]

person_1_age = 20
person_2_age = 30
# creating a list based on variables
age_list = [person_1_age, person_2_age]

# List within a List 
list_within_a_list = [["red", "green", "blue"], ["yellow", "orange", "purple"]]

# Task: Creating a List
city_list = ["Glasgow", "London", "Edinburgh"]

print('\n\n')

"""Exercise 2"""
# Accessing a List

# using the string list from exercise 1

# indices start from 0, so the second element is at index 1
second_item = string_list[1]

# Slicing

# this slice from 0 to 2 gives the first two elements of index 0 and 1
print(string_list[0:2])

# using negative indices
last_item = string_list[-1]  # last item is at index -1

# Task

# Third item
print(city_list[2])       
# Last two items using slicing
print(city_list[1:])      


print('\n\n')



"""Exercise 3"""
# Modifying a List

# changing the first item (replacement)
string_list[0] = "pear" 

# adding an item to the end of the list
string_list.append("orange") 



# Task

# Adding an item to list - at the end
city_list.append("Manchester")

# Modifying an item at index 1 - second element
city_list[1] = "Birmingham"


print('\n\n')


"""Exercise 4"""

# Task: Create, Access and Modify Lists
print("Task: Create, Access and Modify Lists\n")

# Creating a list of colours
colours = ["blue", "green", "yellow"]

# Showing the full list
print("All colours:", colours)

# Printing the second item in the list
print("Second colour:", colours[1])

# Changing the first colour in the list
colours[0] = "purple"

# Showing the updated list
print("Modified colours:", colours)

# Printing how many items are in the list
print("Number of colours in the list:", len(colours))

# Checking if 'red' is in the list
if "red" in colours:
    print("Colour 'Red' is present in the list")
else:
    print("Colour 'Red' is not present in the list")

# Making a new list from 2nd and 3rd colours
selected_colours = colours[1:3]

# Showing the new small list
print("Selected colours:", selected_colours)

print('\n\n')


""" 
-------- Section 3: Python Loops --------

"""


"""Exercise 1"""
# While Loop
i = 0
while i < 5:
    print(i)
    i += 1

print('\n\n')


"""Exercise 2"""
# For Loop
for fruit in string_list:
    print(fruit)

print('\n\n')


# Task
# loop for city list
for city in city_list:
    print(city)

print('\n\n')


"""Exercise 3"""
# Loop Keywords: Range, break and continue

# range()
# function to generate a series of numbers to use in a for loop
# or want to perform a task a certain number of times
for number in range(1, 6):
    print(number)
    
# break
# it will stop the loop from running any more iterations
for i in range(5):
    if i == 2:
        break   
    print(i)

# Task: print the numbers 0 through 4, but stop the loop when i is equal to 3
for i in range(5):
    if i == 3:
        break
    print(i)

# Continue
# it will skip the current iteration and continue to the next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)
    
print('\n\n')


"""Exercise 4"""

# Task: Print Even Numbers from a List
print("Task: Print Even Numbers from a List\n")

# A simple list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through the list and print only even numbers
print("Even numbers in the list:")
for num in numbers:
    if num % 2 == 0:
        print(num)

print('\n\n')

# Task: Sum of Squares
print("Task: Sum of Squares\n")

# Starting the total from 0
sum_of_squares = 0

# Going from 1 to 5 and adding each number squared
for number in range(1, 6):
    sum_of_squares += number * number

# Showing the final result
print("The sum of squares from 1 to 5 is:", sum_of_squares)

print('\n\n')

# Task: Countdown from 10 to 1 using while loop
print("Task: Countdown from 10 to 1 using while loop\n")

# Start countdown at 10
countdown = 10

# Keep counting down till 1
while countdown >= 1:
    print(countdown)
    countdown -= 1

# Once done, show this message
print("Liftoff!")

print('\n\n')

"""

-------- Section 4: Obtaining User Input --------

"""

# input()
# function is used to take input from the user
user_input = input("Enter something: ")
print("You entered:", user_input)


# Example - entering a number
age = input("How old are you? ")
# Convert the age to an integer
age = int(age)
next_year_age = age + 1
print("Next year, you'll be", next_year_age, "years old.")

print('\n\n')

# Task: User Input and Conditionals
print("Task: User Input and Conditionals\n")

# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check which age group they belong to
if age < 18:
    print("You are a minor.")
elif age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


print('\n\n')

# Task: Temperature Converter with user input and options
print("Task: Temperature Converter with user input and options\n")

while True:
    # Ask the user what type of temperature they want to convert
    choice = input("Enter the temperature unit you want to convert from (C, F, or K): ").upper()

    # If the choice is valid, go ahead
    if choice in ["C", "F", "K"]:
        # Ask for the temperature value
        temp = float(input("Enter the temperature value: "))

        # Convert based on the unit entered
        if choice == "C":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            print(f"\n{temp}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f}K.")
        
        elif choice == "F":
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15
            print(f"\n{temp}°F is equal to {celsius:.2f}°C and {kelvin:.2f}K.")
        
        elif choice == "K":
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            print(f"\n{temp}K is equal to {celsius:.2f}°C and {fahrenheit:.2f}°F.")

        # Break the loop once conversion is done
        break

    else:
        # Tell the user to enter a valid unit
        print("\nInvalid input. Please enter C, F, or K.\n")

print("="*40)
