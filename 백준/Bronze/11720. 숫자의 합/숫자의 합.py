N = int(input())
num = str(input())

lst = []

# '12345' -> 1, 2, 3, 4, 5

for i in num:
    lst.append(int(i))

print(sum(lst))