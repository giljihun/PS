import sys

box = []

for _ in range(9):
    dummy = list(map(int ,sys.stdin.readline().split()))
    box.append(dummy)

clone = sum(box, [])
clone.sort()
target = clone[-1]

for i in range(len(box)):
    for j in range(len(box)):
        if box[i][j] == target:
            print(target)
            print(i+1, j+1)