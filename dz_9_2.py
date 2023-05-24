# Написать функцию, которая принимает на вход два списка чисел и возвращает новый список,
# содержащий суммы соответствующих элементов этих списков.

def sum_list_items(lst_1: list, lst_2: list) -> list:
    while len(lst_1) != len(lst_2):
        lst_2.append(0) if len(lst_1) > len(lst_2) else lst_1.append(0)
    return list(map(lambda n_1, n_2: n_1 + n_2, lst_1,lst_2))


print(sum_list_items([1,1,1,6,8],[3,3,3]))
