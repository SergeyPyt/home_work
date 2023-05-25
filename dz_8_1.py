# Напишите функцию, которая принимает строку и возвращает список
# всех уникальных символов в этой строке.

str_ca = "dkfjnbkdnbk"


def uni_sym(str_cy: str) -> list:
    lst_new = []
    for symbol in str_ca:
        if str_ca.count(symbol) == 1:
            lst_new.append(symbol)
    return lst_new


print(uni_sym(str_ca))


