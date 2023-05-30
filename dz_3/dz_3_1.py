#"1 2 3 4 5" найдите самое большое и маленькое
# число в этой строке и верните их кортежем.

array = input("Введите числа через пробел: ")
array_lst = array.split()
array_lst = list(map(int, array_lst))
array_tpl = tuple(array_lst)
print(max(array_tpl), min(array_tpl))
