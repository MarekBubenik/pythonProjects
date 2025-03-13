#students = ["Hermione","Harry", "Ron"]
# # print(students[0])
# for student in students:
#     print(student)

# for i in range(len(students)):      # len = length
#     print(i, students[i])

#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

students = {
    "Hermione": "Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin"
}                                   # dictionary, associate it with something, indexes are literal, not numeric as opose to list

# print(students["Draco"])
# print(students["Harry"])
# print(students["Ron"])

for student in students:
    print(student, students[student], sep=", ")
