import sys

N, M = map(int, sys.stdin.readline().split())

basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    temp1 = basket[:i-1]
    real_temp = basket[i-1:j]
    real_temp.reverse()
    temp2 = basket[j:]

    basket = temp1 + real_temp + temp2

print(*basket)