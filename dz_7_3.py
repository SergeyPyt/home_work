# Написать функцию, которая принимает список дат в
# формате 'ДД.ММ.ГГГГ' и возвращает список дат в
# формате 'ГГГГ-ММ-ДД', отсортированный по возрастанию.

date_list = ["09.03.2005", "10.04.2001", "08.04.1999"]


def date_sort(dt: list) -> list:
    date_list_upd = []
    for date in dt:
        date_list_upd.append("-".join(date.split(".")[::-1]))
    return sorted(date_list_upd)


print(date_sort(date_list))



