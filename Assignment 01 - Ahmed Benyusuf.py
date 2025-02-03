import random
import statistics
import math
from functools import reduce

# Creates an array of 80 random numbers between 1 and 85
numbers = [random.randint(1, 85) for _ in range(80)]

# Prints out the numbers in 8 lines of 10 numbers, evenly spaced
print("Original Numbers:")
for i in range(0, 80, 10):
    print(" ".join(f"{num:2}" for num in numbers[i:i+10]))

# Sorts the numbers in ascending order
sorted_numbers = sorted(numbers)

# Prints the sorted numbers in 8 lines of 10 numbers
print("\nSorted Numbers:")
for i in range(0, 80, 10):
    print(" ".join(f"{num:2}" for num in sorted_numbers[i:i+10]))

# Finds and print the smallest number in the array
smallest = min(sorted_numbers)
print(f"\nSmallest Number: {smallest}")

# Finds and print the largest number in the array
largest = max(sorted_numbers)
print(f"Largest Number: {largest}")

# Determines and prints the sum of the numbers
sum_numbers = sum(sorted_numbers)
print(f"Sum of Numbers: {sum_numbers}")

# Determines and prints the product of the numbers
product_numbers = reduce(lambda x, y: x * y, sorted_numbers)
print(f"Product of Numbers: {product_numbers}")

# Calculates the mean, median, and mode
mean = round(statistics.mean(sorted_numbers), 3)
median = statistics.median(sorted_numbers)
mode = statistics.multimode(sorted_numbers)

print(f"\nMean: {mean}")
print(f"Median: {median}")
if mode:
    print(f"Mode: {', '.join(map(str, mode))}")
else:
    print("Mode: None")

# Calculates and prints the standard deviation
std_dev = round(statistics.stdev(sorted_numbers), 3)
print(f"Standard Deviation: {std_dev}")
