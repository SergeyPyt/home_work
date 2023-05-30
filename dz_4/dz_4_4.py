# С клавиатуры вводится натуральное число. Найти его наибольшую
# цифру. Например, введено число 764580. Наибольшая цифра в нем 8.

num = int(input("Enter a number: "))
str_num = str(num)
lst_num = list(str_num)
print(max(lst_num))
