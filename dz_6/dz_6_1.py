#Напишите функцию sum_range(start, end), которая суммирует
# все целые числа от значения «start» до величины «end» включительно.
num_1 = int(input("Enter a 1 number: "))
num_2 = int(input("Enter a 2 number: "))


def sum_range(start, end):
    if start > end:
        start, end = end, start
    counter = 0
    while start <= end:
        counter += start
        start += 1
    return counter


print(sum_range(num_1,num_2))

