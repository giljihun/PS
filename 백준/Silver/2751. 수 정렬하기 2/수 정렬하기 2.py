# boj 2751, 수 정렬하기 2
# 240129

import sys

N = int(sys.stdin.readline())

nums = []
for _ in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)

nums.sort()

for num in nums:
    print(num)