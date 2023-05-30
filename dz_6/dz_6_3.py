#Написать функцию, принимающую число и возвращающую ближайший
# к этому числу палиндром.  11 -> 22,  188 -> 191,  191 -> 202, 2541 -> 2552
num = int(input("Enter a number: "))


def palindrome(n):
    while str(n) != str(n)[::-1]:
        n += 1
    return n


print(palindrome(num))

