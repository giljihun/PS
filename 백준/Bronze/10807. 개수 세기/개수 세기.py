N = int(input())
lst = list(map(int, input().split()))
v = int(input())

answer = 0

for index in lst:
    if int(index) == v:
        answer += 1

print(answer)