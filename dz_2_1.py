'''Написать программу, которая удаляет первый и последний символы строки.
Если строка содержит меньше  двух символов - вывести сообщение об ошибке. '''
s = input()
if len(s) >=2:
    s = s[1:-1]
    print(s)
else:
    raise ValueError("Incorrect ..")