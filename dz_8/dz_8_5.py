# Напишите функцию, которая принимает на вход список списков чисел и
# возвращает новый список, содержащий те же числа, но увеличенные на 1.

lst = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]


def subs(lst_num: list) -> list:
    lst_new = []
    for element in lst_num:
        a = []
        for num in element:
            a.append(num+1)
        lst_new.append(a)
    return lst_new


print(subs(lst))
