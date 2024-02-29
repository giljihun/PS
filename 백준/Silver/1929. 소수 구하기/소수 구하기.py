import sys
import math

M, N = map(int, sys.stdin.readline().split())

# 소수 -> 나눠지는 수가 자기 자신과 1 밖에 없어야함.
def primeNUM(num):
    if num == 1:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

for num in range(M, N+1):
    if primeNUM(num):
        print(num)