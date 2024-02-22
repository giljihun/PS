import sys

N = int(sys.stdin.readline())
people = []
answer = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    people.append((x, y))

for i in range(N):
    cnt = 0
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    answer.append(cnt + 1)

print(*answer, sep=' ')