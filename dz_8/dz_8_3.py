#Напишите функцию, которая принимает на вход список чисел и возвращает новый список,
# содержащий только те числа, которые больше среднего значения всех чисел в списке.

lst = [1, 2, 4, 3, 45, 7, 19, 54, 98,26,27,28,34]


def averague_num(lst_num: list) -> list:
    lst_new = []
    average_value = sum(lst_num) / len(lst_num)
    for num in lst:
        if num > average_value:
            lst_new.append(num)
    return lst_new


print(sorted(averague_num(lst)))
