# Даны два целых числа A и В. Выведите все числа от A до B
# включительно, в порядке возрастания, если A < B,
# или в порядке убывания в противном случае.

a = 10
b = 1
lst = []
if a < b:
    while a <= b:
        lst.append(a)
        a += 1
elif a > b:
    while a >= b:
        lst.append(a)
        a -= 1
else:
    print(f"{a} = {b}")
print(lst)
