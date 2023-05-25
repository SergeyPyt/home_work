# Написать функцию, которая принимает список словарей, где каждый словарь представляет
# собой запись об ученике (с ключами 'имя', 'возраст', 'оценки'), и возвращает список словарей,
# отсортированный по возрасту учеников в порядке убывания средней оценки каждого ученика.

students = [{"name": "Walter", "age": 18, "gpa": 99},
            {"name": "Bob", "age": 20, "gpa": 95},
            {"name": "Aleks", "age": 19, "gpa": 97},
            {"name": "Peter", "age": 18, "gpa": 91},
            {"name": "Viktor", "age": 20, "gpa": 94}
            ]


def sort_gpa(dct: dict):
    return dct["gpa"]


def sort_age(dct: dict):
    return dct["age"]


def custom_sort(stud: list) -> list:
    sorted_gpa = sorted(stud, key=sort_gpa, reverse=True)
    return sorted(sorted_gpa, key=sort_age, reverse=True)


print(custom_sort(students))
