# Напишите функцию, которая принимает на вход список строк и возвращает новый список,
# содержащий те же строки, но с замененным первым символом на символ '*' (например, "hello" станет "*ello").

lst = ["xuy", "chln", "glaz", "oko", "yho", "nos"]


def subs_symbol(lst_sym: list) -> list:
    lst_new = []
    symbol = "*"
    for line in lst_sym:
        lst_new.append(symbol + line[1:])
    return lst_new


print(subs_symbol(lst))


