n = int(input())

s = ""
for i in range(n):
    s += chr(ord("a") + i)

print(list(s))