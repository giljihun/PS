import sys
from collections import deque
import math

def roundup(num):
    if (num - (math.trunc(num)) == 0.5):
        return math.ceil(num)
    else:
        return round(num)

n = int(sys.stdin.readline())
rank = []

if n == 0:
    print(0)
else:
    for i in range(n):
        rank.append(int(sys.stdin.readline()))

    rank.sort()
    rank = deque(rank)

    p_avg = roundup(len(rank) * 15 / 100)

    for _ in range(p_avg):
        rank.popleft()
        rank.pop()

    print(roundup(sum(rank) / len(rank)))