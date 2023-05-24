#Написать функцию, которая принимает список и считает
# кол-во одинаковых элементов в нем.

from collections import Counter

def count(array):
    res = 0
    counter_array = Counter(array).values()
    for num in counter_array:
        if num != 1:
            res += 1
    return res


lst = ["c", "b", "v", "a", "v", "a"]
print(count(lst))
