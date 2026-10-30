"""Loops in Python: theory and examples

A loop repeats a block of code, avoiding repeated instructions. Python's two
main loop types are:

* `for` loops visit each item in a sequence, such as a list or range. Use one
	when you want to process a known collection of items.
* `while` loops repeat while a condition is True. Use one when repetition
	depends on a condition. Change that condition in the loop so it can stop.

The indented statements under a loop form its body and run on each repetition.
"""

# A for loop with range: the end value (6) is not included, so this prints 1–5.
for number in range(1, 6):
		print(number)

# A for loop can also visit each item in a list.
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
		print("I like", fruit)

# A while loop repeats as long as count > 0. Decreasing count makes it stop.
count = 3
while count > 0:
		print("Countdown:", count)
		count -= 1
print("Go!")
