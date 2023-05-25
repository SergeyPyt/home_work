# Напишите функцию, которая принимает на вход список строк и возвращает новый список,
# содержащий только те строки, которые начинаются с буквы 'a' (большой или малой).

lst = ["hkdhhdh", "akdgdlkdnlb", "gdshs", "Aghdh", "afhdf", "hjgdjdjg", "Adndfdfgnd"]


def sort_lst(lst_str: list) -> list:
    lst_new = []
    for line in lst_str:
        if line.startswith("A") or line.startswith("a"):
            lst_new.append(line)
    return lst_new


print(sort_lst(lst))
