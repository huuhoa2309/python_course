student= [
    {"name": "Hoa", "class": "A", "age": 10},
    {"name": "Bao", "class": "B", "age": 20},
    {"name": "Anh", "class": "E", "age": 11},
    {"name": "Vy", "class": "G", "age": 9},
]
# def sort_by_name(student):
#     return student["name"]

student.sort(key=lambda student: student["age"])
print(student)