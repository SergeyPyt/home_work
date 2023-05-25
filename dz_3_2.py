#Написать программу, которая может принимать
# любое неотрицательное целое число в качестве
# аргумента и возвращать новое максимально возможное значение,
# составленное из цифр этого же числа. По сути, просто
# переставить цифры, чтобы создать максимально возможное число.
num = int(input("Enter a number: "))
num_lst = []
lastnum = 0
while num != 0:
    lastnum = num%10
    num_lst.append(lastnum)
    num = num//10
num_lst.sort()
num_lst.reverse()
num_lst = list(map(str, num_lst))
num_str = "".join(num_lst)
print(num_str)
