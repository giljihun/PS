import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

# 2 1 5
answer = (V-B) / (A-B)

print(math.ceil(answer))