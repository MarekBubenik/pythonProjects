# with open("students.csv") as file:
#     for line in file:
#         row, house = line.rstrip().split(",")
#         print(f"{row} is in {house}")

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split()
        student = {}
        student["name"] = name
        student["house"] = house

