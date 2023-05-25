# Есть число n, вывести первые n чисел последовательности Фибоначчи.

f_1 = f_2 = 1
n = int(input("Enter: "))
i = 2
print(f_1, f_2, end=" ")
while i < n:
    f_1, f_2 = f_2, f_1 + f_2
    print(f_2, end=" ")
    i += 1
