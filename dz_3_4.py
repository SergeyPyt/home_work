#С клавиатуры вводится натуральное число.
# Найти его наибольшую цифру.
# Например, введено число 764580. Наибольшая цифра в нем 8.
num = int(input())
num_lst = []
lastnum = 0
while num != 0:
    lastnum = num%10
    num_lst.append(lastnum)
    num = num//10
num_tpl = tuple(num_lst)
print(max(num_tpl))
