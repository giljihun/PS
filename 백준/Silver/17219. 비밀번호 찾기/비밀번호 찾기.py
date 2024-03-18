import sys

N, M = map(int, sys.stdin.readline().split())

library = {}

for _ in range(N):
    address, pw = map(str, sys.stdin.readline().split())
    library[address] = pw

answer = []

for _ in range(M):
    target = str(input())
    answer.append(library[target])

for ans in answer:
    print(ans)
