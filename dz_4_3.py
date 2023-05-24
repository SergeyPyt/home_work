# Передается список, состоящий из строк и букв, нужно вернуть
# новый список, содержащий только цифры.

lst = ["s", "v", 2, 6, 1, 8, "v"]
lst_new = []
for element in lst:
    if type(element) == int:
        lst_new.append(element)
print(lst_new)
