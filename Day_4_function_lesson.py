"Day 4 lesson: Functions in Python learn with Mahek Geete"
"""Functions in Python: theory and examples

A function is a named, reusable block of code that performs a task. Functions
help organize a program and avoid writing the same instructions repeatedly.

Define a function with `def`, followed by its name and parentheses. The
indented lines below the definition are its body. Defining a function does
not run it; call it by writing its name followed by parentheses.

Parameters are the input names written in the definition. Arguments are the
actual values passed in when the function is called. A function can send a
result back to its caller with `return`.
"""


# This function has no parameters and prints a greeting when called.
def say_hello():
    print("Hello! Welcome to Python functions.")


say_hello()


# `name` and `age` are parameters; "Asha" and 20 are arguments.
def introduce(name, age):
    print("My name is", name, "and I am", age, "years old.")


introduce("Asha", 20)


# `return` gives the result back so the caller can store or use it.
def add_numbers(first_number, second_number):
    return first_number + second_number


total = add_numbers(5, 3)
print("The sum is", total)


# A parameter can have a default value, used when no argument is provided.
def greet(name="friend"):
    print("Hi,", name)


greet()
greet("Sam")