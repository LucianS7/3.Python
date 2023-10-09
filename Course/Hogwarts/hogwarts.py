students = {
    "a" : {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
    "b" : {"name2": "Harry", "house": "Griffindor", "patronus": "Stag"},
    "c" : {"name1": "Ron", "house": "Griffindor", "patronus": "Jack Russell terrier"},
    "d" : {"name3": "Draco", "house": "Slytherin", "patronus": None}
}

#for student in students:
#    print(student["name"], student["house"], student["patronus"], sep=", ")

for i in students:
    first_pair = list(students[i].items())[0]
    print(f"{first_pair[0]} : {first_pair[1]}")




students_2 = [
    {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

#for student in students:
#    print(student["name"], student["house"], student["patronus"], sep=", ")

#for i in students_2:
#    print(i)