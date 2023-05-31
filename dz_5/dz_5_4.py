# Написать программу, которая будет конвертировать строку в CamelCase.
# Например:
# "the-stealth-warrior" -> "theStealthWarrior"
# "The_Stealth_Warrior" -> "TheStealthWarrior"
# "The_Stealth-Warrior" -> "TheStealthWarrior"

element = "-_"
line = "the-stealth_warrior"

for i in line:
    if i in element:
        line = line.replace(i, " ")

lst = [line.split()[0]]

for j in line.split()[1:]:
    lst.append(j.capitalize())
print("".join(lst))
