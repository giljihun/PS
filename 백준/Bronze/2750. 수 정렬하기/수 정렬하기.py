import sys

N = int(sys.stdin.readline())
answer = []
for _ in range(N):
    answer.append(int(input()))

answer.sort()

for ans in answer:
    print(ans)