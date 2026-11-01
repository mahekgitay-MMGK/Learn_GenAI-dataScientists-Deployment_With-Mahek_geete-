"""Day 5 lesson: Lists and dictionaries in Python

Lists and dictionaries are containers: they let one variable hold a group of
related values.

Use a list when you care about the order of items or need to access them by
position. Use a dictionary (often called a dict) when each value should be
found using a meaningful key, such as a person's name or a product ID.

Both are mutable, which means you can change them after creating them.
"""


# ---------------------------------------------------------------------------
# 1. Lists
# ---------------------------------------------------------------------------

# A list is an ordered, changeable collection. Square brackets create a list.
# Lists can contain different kinds of values, and they can contain duplicates.
fruits = ["apple", "banana", "mango", "banana"]
print("Fruit list:", fruits)

# Each item has a zero-based index: the first item is at index 0.
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Negative indexes count backward from the end: -1 is the last item.
print("Last fruit:", fruits[-1])

# A slice selects a range. The start is included and the stop is excluded.
print("Items at indexes 1 and 2:", fruits[1:3])
print("First two fruits:", fruits[:2])
print("From index 2 to the end:", fruits[2:])

# Lists are mutable: assignment at an index replaces that item.
fruits[0] = "pear"
print("After replacing index 0:", fruits)

# Add one item with append; add each item from another collection with extend.
fruits.append("orange")
fruits.extend(["grape", "kiwi"])
print("After append and extend:", fruits)

# insert adds an item at a chosen position and shifts later items right.
fruits.insert(1, "plum")
print("After insert:", fruits)

# remove deletes the first matching value; pop removes and returns by position.
fruits.remove("banana")
removed_fruit = fruits.pop()
print("Removed with pop:", removed_fruit)
print("After remove and pop:", fruits)

# len counts items; `in` checks whether a value is present.
print("Number of fruits:", len(fruits))
print("Is mango in the list?", "mango" in fruits)

# A for loop visits values in list order.
print("Fruit names:")
for fruit in fruits:
    print("-", fruit)

# sort changes the existing list; sorted(...) makes a new sorted list.
scores = [82, 95, 71, 88]
scores.sort()
print("Scores sorted in place:", scores)
scores_descending = sorted(scores, reverse=True)
print("A separate descending order:", scores_descending)

# Assignment does not copy a list: both names refer to the same list.
original = ["red", "blue"]
same_list = original
same_list.append("green")
print("Original after changing its alias:", original)

# copy() creates a separate outer list for simple, one-level lists.
separate_list = original.copy()
separate_list.append("yellow")
print("Original after changing its copy:", original)
print("Copied list:", separate_list)


# ---------------------------------------------------------------------------
# 2. Dictionaries
# ---------------------------------------------------------------------------

# A dictionary stores key:value pairs. Keys are unique; values can repeat.
# Curly braces with key:value pairs create a dictionary.
student = {
    "name": "Asha",
    "age": 20,
    "course": "Python",
}
print("\nStudent dictionary:", student)

# Use a key, not a numeric position, to look up a dictionary value.
print("Student name:", student["name"])
print("Student age:", student["age"])

# Bracket lookup raises KeyError if the key is missing. get() lets you provide
# a fallback value instead.
print("Student city:", student.get("city", "Not provided"))

# Add a new key or change an existing key by assignment.
student["city"] = "Pune"
student["age"] = 21
print("After adding city and changing age:", student)

# update() can add or change several pairs in one operation.
student.update({"course": "Data Science", "active": True})
print("After update:", student)

# `in` checks dictionary keys, not values.
print("Does student have an email key?", "email" in student)
print("Is Pune one of the values?", "Pune" in student.values())

# keys(), values(), and items() provide views of the dictionary contents.
print("Keys:", student.keys())
print("Values:", student.values())
print("Key/value pairs:", student.items())

# Looping over a dictionary directly visits its keys.
print("Student details:")
for key, value in student.items():
    print(key, "=", value)

# pop removes a key and returns its value. del also removes a key, but does
# not return the removed value.
removed_course = student.pop("course")
print("Removed course:", removed_course)
del student["active"]
print("After removing course and active:", student)

# Dictionaries preserve insertion order in modern Python (Python 3.7+).
# Reassigning an existing key changes its value without adding a second key.
student["name"] = "Asha Shah"
print("Updated student:", student)


# ---------------------------------------------------------------------------
# 3. Choosing between a list and a dictionary
# ---------------------------------------------------------------------------

# A list is a good fit when position/order matters and items are alike.
weekly_temperatures = [22, 24, 23, 25]
print("\nTuesday's temperature:", weekly_temperatures[1])

# A dictionary is a good fit when a value has a descriptive label.
temperatures_by_day = {
    "Monday": 22,
    "Tuesday": 24,
    "Wednesday": 23,
    "Thursday": 25,
}
print("Tuesday's temperature:", temperatures_by_day["Tuesday"])

# Lists and dictionaries can be combined. This list contains dictionaries,
# which is a common way to represent records such as products or people.
classroom = [
    {"name": "Asha", "score": 92},
    {"name": "Ravi", "score": 85},
]
print("\nFirst student's name:", classroom[0]["name"])
for record in classroom:
    print(record["name"], "scored", record["score"])


# ---------------------------------------------------------------------------
# 4. Quick recap
# ---------------------------------------------------------------------------

# List: ordered items, access by index, written with [].
# Dictionary: key:value pairs, access by key, written with {}.
# Both can be changed in place, looped over, and nested inside other containers.