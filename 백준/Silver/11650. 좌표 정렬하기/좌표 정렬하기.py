import sys

N = int(sys.stdin.readline())

target = []
for i in range(N):
    x, y = map(int, input().split())
    target.append((x, y))

target.sort()


for t in target:
    print(t[0], t[1])



