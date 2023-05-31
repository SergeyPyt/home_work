# Напишите декоратор timer, который измеряет время выполнения
# функции и выводит его на экран. Используйте модуль time для измерения времени.

from datetime import datetime
from sympy import isprime


def benchmark(func):
    def measuring_time():
        start = datetime.now()
        func()
        print(datetime.now() - start)
    return measuring_time


@benchmark
def custom_sort():
    result = []
    for num in range(100_000):
        if isprime(num):
            result.append(num)


@benchmark
def custom_sort_func():
    lst = list(filter(lambda num: isprime(num), range(100_000)))


print(f"Время работы цикла: {custom_sort_func()}")
print(f"Время работы цикла: {custom_sort()}")
