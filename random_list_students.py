from random import randint


names = ["Tracey", "Sarah", "Joanne", "Sharon"]
surnames = ["Abramson", "Hoggarth", "Adamson", "Holiday"]

name_count = len(names)
surname_count = len(surnames)


def students_generator(counter: int):
    result = []
    for _ in range(counter):
        name_surname = names[randint(0,name_count - 1)] + " " + surnames[randint(0, surname_count - 1)]
        age = randint(14, 18)
        gpa = randint(0, 100)
        students = {"Fullnames": name_surname, "Age": age, "Gpa": gpa}
        result.append(students)
    return result


for i in students_generator(10):
    print(i)


