#Передается список, состоящий из строк и букв,
# нужно вернуть новый список, содержащий только цифры.
lst = [1, "a", 4, "g", 7, "hfg"]
lst_new = []
for i in lst:
    if type(i) == int:
        lst_new.append(i)
print(lst_new)

