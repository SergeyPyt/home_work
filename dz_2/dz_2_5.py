'''Вы вводите с клавиатуры последовательность чисел, разделённых запятой.
Составьте список и кортеж с этими числами.'''
array = input("Введите числа: ")
array_lst = list(map(int, array.split(",")))
array_tpl = tuple(array_lst)
print(array_lst, array_tpl)
