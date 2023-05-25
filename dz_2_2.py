'''Напишите программу которая настроит отображение комментария к отметке 'мне нравится' в условном посте. Список имен передается в кач-ве аргумента.
Например:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this" '''

names = ["Peter", "Jacob", "Alex", "John"]
if len(names) == 0:
    print("No one like this")
elif len(names) == 1:
    print(f"{names[0]} like this.")
elif len(names) == 2:
    print(f"{names[0]} and {names[1]} like this.")
elif len(names) == 3:
    print(f"{names[0]}, {names[1]} and {names[2]}")
else:
    print(f"{names[0]},{names[1]} and {len(names)-2} like this")
