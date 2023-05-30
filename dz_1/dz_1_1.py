# При заданном целом числе n посчитайте n + nn + nnn. Например, если n = 3, нужно посчитать сумму 3 + 33 + 333 и вывести результат)
num = input('Enter a number:')
summ = (int(num)+int(num*2)+int(num*3))
print(summ)
