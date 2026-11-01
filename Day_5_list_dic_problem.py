#list - many sudents

student_data=["Mahek","Asha","Riya","Anvi","Sana","Tanya"]
print("Name",student_data[0])

# dictionary - many students with their details

student_data={"Name":"Mahek","Mark": 90,"Grade":"A","Course":"Python","Active":True,},
{"Name":"Asha","Mark": 80,"Grade":"B","Course":"Python","Active":True,},
{"Name":"Riya","Mark": 70,"Grade":"C","Course":"Python","Active":True,}

print(student_data[0])

# list of dictionaries - many students with their details
student_data=[
    {"Name":"Mahek","Mark": 90,"Grade":"A","Course":"Python","Active":True},
    {"Name":"Asha","Mark": 80,"Grade":"B","Course":"Python","Active":True},
    {"Name":"Riya","Mark": 70,"Grade":"C","Course":"Python","Active":True}
]
print(student_data[0])

#problem checking who is topper

student_data = [
    {"Name": "Mahek", "Mark": 92, "Grade": "A"},
    {"Name": "Asha", "Mark": 84, "Grade": "B"},
    {"Name": "Riya", "Mark": 76, "Grade": "C"},
    {"Name": "Anvi", "Mark": 68, "Grade": "D"},
    {"Name": "Sana", "Mark": 95, "Grade": "A"},
    {"Name": "Tanya", "Mark": 81, "Grade": "B"},
    {"Name": "Arjun", "Mark": 73, "Grade": "C"},
    {"Name": "Neha", "Mark": 59, "Grade": "F"},
    {"Name": "Kabir", "Mark": 88, "Grade": "B"},
    {"Name": "Meera", "Mark": 90, "Grade": "A"},
    {"Name": "Ishaan", "Mark": 67, "Grade": "D"},
    {"Name": "Diya", "Mark": 79, "Grade": "C"},
    {"Name": "Rahul", "Mark": 86, "Grade": "B"},
    {"Name": "Priya", "Mark": 54, "Grade": "F"},
    {"Name": "Dev", "Mark": 98, "Grade": "A"},
    {"Name": "Kavya", "Mark": 71, "Grade": "C"},
    {"Name": "Aarav", "Mark": 63, "Grade": "D"},
    {"Name": "Nisha", "Mark": 83, "Grade": "B"},
    {"Name": "Vivaan", "Mark": 91, "Grade": "A"},
    {"Name": "Ira", "Mark": 77, "Grade": "C"},
    {"Name": "Rohan", "Mark": 58, "Grade": "F"},
    {"Name": "Pooja", "Mark": 89, "Grade": "B"},
    {"Name": "Aditya", "Mark": 65, "Grade": "D"},
    {"Name": "Simran", "Mark": 94, "Grade": "A"},
    {"Name": "Yash", "Mark": 72, "Grade": "C"},
    {"Name": "Anaya", "Mark": 87, "Grade": "B"},
    {"Name": "Om", "Mark": 61, "Grade": "D"},
    {"Name": "Zara", "Mark": 96, "Grade": "A"},
    {"Name": "Kiran", "Mark": 74, "Grade": "C"},
    {"Name": "Mira", "Mark": 52, "Grade": "F"},
]

top_student= student_data[0]
for student in student_data:
    if student["Mark"] > top_student["Mark"]:
        top_student = student

print(f"Top student: {top_student['Name']} with Mark: {top_student['Mark']} and Grade: {top_student['Grade']}")

total=0
for student in student_data:
    total += student["Mark"]
average = total / len(student_data)

print(f"Average Mark of all students: {average:.2f}")