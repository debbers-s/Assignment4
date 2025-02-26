## Part 1: Defining Functions (12 points)

# 1) Basic Function (2 points)
# Write a function add_numbers that takes two numbers and returns their sum. Implement this using both a regular function and a lambda function.
# Test your function with add_numbers(3, 5) and add_lambda(3, 5).

def add_numbers(x,y):
    return x+y
print(f"Regular function: {add_numbers(3,5)}")

add_lambda = lambda x, y: x+y
print(f"Lambda function: {add_lambda(3,5)}")


# 2) Flexible Function (2 points)
# Modify join_words to accept an arbitrary number of words and return them concatenated into a single string with spaces. Implement this using both a regular function and a lambda function.
# Test it with join_words("Hello", "world", "!").

def join_words(*args):
    words = " ".join(args)
    return words

print(join_words("Hello", "world", "!"))

join_words2 = lambda *args: " ".join(args)
print(join_words2("Hello", "world", "!"))


# 3) Recursive Function (2 points)
# Write a recursive function countdown(n) that prints numbers from n to 0. Test it with countdown(5).

def countdown(n):
    print(n)
    if n > 0:
        countdown(n-1)

countdown(5)

# 4) Normal Function Usage (2 points)
# Write a function greet that takes a name as input and returns a greeting message. Implement this as a normal function.
# Test it with greet("Alice").

def greet(name):
    print(f"Good evening, {name}")

greet("Alice")

# 5) Function with Default Arguments (2 points)
# Write a function repeat_phrase that repeats a phrase a given number of times, with a default of 2.
# Test it with repeat_phrase("Hi! ") and repeat_phrase("Hi! ", 3).

def repeat_phrase(phrase, count = 2):
   print("".join(phrase) * count)

repeat_phrase("Hi! ")
repeat_phrase("Hi! ", 3 )

# 6) Higher-Order Function (2 points)
# Write a function apply_function that takes a function and a value as arguments and applies the function to the value.
# Test it with apply_function(lambda x: x.upper(), "hello").

def apply_function(func, val):
    return func(val)

print(apply_function(lambda x: x.upper(), "hello"))

## Part 2: Errors and Exceptions (10 points)

# 7) Handling Errors (3 points)
# Write a function safe_divide(a, b) that divides a by b, but catches the ZeroDivisionError and prints an error message instead of crashing.
# def safe_divide(a, b):
#    try:
 #       return a / b
  #  except ZeroDivisionError:
   #     return "Error: Cannot divide by zero"

def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: division by zero")

safe_divide(2,3)
safe_divide(2,0)

# 8) Custom Exceptions (3 points)
# Write a function check_age(age) that raises a ValueError with the message "Age must be a positive integer" if age is negative or not an integer.

def check_age(age):
    if age < 0:
        raise ValueError("Age must be a positive integer")
    return age

check_age(1)

# 9) Handling Multiple Exceptions (2 points)
# Write a function parse_int(value) that tries to convert a string to an integer and handles ValueError if the conversion fails.

def parse_int(value):
    try:
        integer = int(value)
        return integer
    except ValueError:
        print("Error, failed to convert value to an integer")

parse_int("lol")


# 10) Finally Block (2 points)
# Modify safe_divide to include a finally block that prints "Division attempted".

def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: division by zero")
    finally:
        print("Division attempted")

safe_divide(2,3)
safe_divide(2,0)

## Part 3: Iterators (12 points)

# 11) Using Built-in Iterators (4 points)
# Use the built-in iter and next functions to iterate over a list of numbers [5, 4, 3, 2, 1] manually.

list1 = [5, 4, 3, 2, 1]
i = iter(list1)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

# 12) Using Generator Expressions (4 points)
# Use a generator expression to create an iterator that yields uppercase versions of words in a list. Iterate over it using a for loop.
words = ['meow', 'cola', 'egg']
uppercase = (word.upper() for word in words)
for word in uppercase:
    print(word)


# 13) Custom Iterator Class (2 points)
# Write a custom iterator class Countdown that counts down from a given number to zero.

class Countdown:
    def __init__(self, n):
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

countdown = Countdown(5)
for num in countdown:
    print(num)

# 14) Using itertools (2 points)
# Use the itertools.cycle function to cycle through a list of colors ["red", "blue", "green"]

import itertools

colors = ["red", "blue", "green"]
cycle = itertools.cycle(colors)
for color in range(6):
    print(next(cycle))

print("hello world")
