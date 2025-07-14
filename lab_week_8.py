from abc import ABC, abstractmethod
from random import randint

print("\n\n")
# ---------- Task 1: Tuples ----------
# Swapping values of a and b using tuple unpacking

a = 5
b = 10

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap using tuple (Pythonic way)
a, b = b, a  # This one-liner swaps the values of a and b without needing a temporary variable

print("After swapping:")
print("a =", a)
print("b =", b)


print("\n\n")

# ---------- Task 2: Sets ----------
# Finding common names in two sets

set1 = {"Tom", "Jerry", "Hewey", "Dewey", "Louie"}
set2 = {"Tom", "Garfield", "Snoopy", "Hewey", "Dewey"}

# Use set intersection to get names present in both sets
common_names = set1 & set2  # The & operator gives us only those elements that exist in both sets

print("\nNames in both sets:")
print(common_names)

# ---------- Task 3: Dictionaries ----------
# Function that counts occurrences of items in a list

def histogram(input_list):
    freq_dict = {}  # empty dictionary to store frequencies
    for item in input_list:
        if item in freq_dict:
            freq_dict[item] += 1  # increase count if item already exists
        else:
            freq_dict[item] = 1   # initialize count if item not seen before
    return freq_dict

# Test the function
my_list = [1, 2, 3, 1, 2, 3, 4]
print("\nHistogram output:")
print(histogram(my_list))

# Optional: check with assert to verify correctness
assert histogram(my_list) == {1: 2, 2: 2, 3: 2, 4: 1}



# ---------- Task 4: Abstract Class ----------
class Dice(ABC):  # Inherits from Abstract Base Class
    def __init__(self) -> None:
        self.face = None  # All dice will have a face attribute

    @abstractmethod
    def roll(self) -> int:
        pass  # Child classes must implement this method
    
class SixSidedDice(Dice):
    def roll(self) -> int:
        self.face = randint(1, 6)
        return self.face
    
    
# Roll the dice 1000 times and collect results
dice = SixSidedDice()
results = [dice.roll() for _ in range(1000)]

# Show histogram
print("Six-Sided Dice Histogram (1000 rolls):")
print(histogram(results))




# ---------- Task 5: Inheritance ----------


# New class inheriting from Dice
class TenSidedDice(Dice):
    def roll(self) -> int:
        self.face = randint(1, 10)
        return self.face

# Roll the ten-sided dice 1000 times
ten_dice = TenSidedDice()
results_10 = [ten_dice.roll() for _ in range(1000)]

# Show histogram
print("\nTen-Sided Dice Histogram (1000 rolls):")
print(histogram(results_10))
