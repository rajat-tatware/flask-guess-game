# # A simple lambda to add two numbers    q1
# add = lambda a, b: a + b
# print("Sum using lambda:", {add(18, 34)})

# def square(n):    q2
#     return n ** 2

# numbers = [1, 2, 3, 4, 5]

# # Using map with a named function
# squared = list(map(square, numbers))

# print("Original:" ,numbers)
# print("Squared:" ,  squared)

# def is_even(n):     q3
#     return n % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Using filter with a named function
# evens = list(filter(is_even, numbers))

# print("Original:", numbers)
# print("Evens: ",  evens)

# from functools import reduce

# def add_together(a, b):
#     return a + b

# numbers = [10, 20, 30, 40 ,50]

# # Using reduce with a named function
# total_sum = reduce(add_together, numbers)

# print("List:", numbers)
# print("Sum: ", total_sum)


# First, let's create a sample file to search through
# First, let's create a sample file to search through
# Step 1: Create a source file with some data
with open("data.txt", "a") as f:
    f.write("\nThis is an appended line.")
print("New line added.")