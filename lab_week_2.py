"""
Python File that contains all the Tasks from Week 2 lab.
Each task is labeled clearly and separated properly for better understanding.
"""

# Task 1: Compare Temperatures
print("="*40)
print("Task 1: Compare Temperatures\n")

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

print("="*40)

# Task 2: Create, Access and Modify Lists
print("Task 2: Create, Access and Modify Lists\n")

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

print("="*40)

# Task 3: Print Even Numbers from a List
print("Task 3: Print Even Numbers from a List\n")

# A simple list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through the list and print only even numbers
print("Even numbers in the list:")
for num in numbers:
    if num % 2 == 0:
        print(num)

print("="*40)

# Task 4: Sum of Squares
print("Task 4: Sum of Squares\n")

# Starting the total from 0
sum_of_squares = 0

# Going from 1 to 5 and adding each number squared
for number in range(1, 6):
    sum_of_squares += number * number

# Showing the final result
print("The sum of squares from 1 to 5 is:", sum_of_squares)

print("="*40)

# Task 5: Countdown from 10 to 1 using while loop
print("Task 5: Countdown from 10 to 1 using while loop\n")

# Start countdown at 10
countdown = 10

# Keep counting down till 1
while countdown >= 1:
    print(countdown)
    countdown -= 1

# Once done, show this message
print("Liftoff!")

print("="*40)

# Task 6: Take age input from the user and give a message
print("Task 6: Take age input from the user and give a message\n")

# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check which age group they belong to
if age < 18:
    print("You are a minor.")
elif age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

print("="*40)

# Task 7: Temperature Converter with user input and options
print("Task 7: Temperature Converter with user input and options\n")

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
