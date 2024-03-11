book = []
student = []
nope = []

for i in range(1, 31):
    book.append(i)

for i in range(28):
    student.append(int(input()))

for man in book:
    if man not in student:
        nope.append(man)

nope.sort()

print(nope[0])
print(nope[1])