# 3*. Дан список чисел. Реализуйте "bubble sort" для этого списка
# и верните, получившееся значение.

lst = [1, 2, 3, 12, 6, 8, 124]
ln = len(lst)

for _ in range(ln):
    for j in range(ln - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j +1], lst[j]

print(lst)
