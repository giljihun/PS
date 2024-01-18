# 1874

n = int(input())

stack = []
result = []
cango = True

# 오름차순이기때문에 1부터 항상 넣어야함.
current = 1

for _ in range(n):

    num = int(input())

    while current <= num:

        stack.append(current)
        result.append('+')
        current += 1

    if stack[-1] == num:

        stack.pop()
        result.append('-')

    else:
        cango = False

if cango:
    for i in result:
        print(i)

else:
    print('NO')