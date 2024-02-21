N, M = map(int, input().split())
basket = [0] * N

for cnt in range(M):
  i, j, k = map(int ,input().split())
  for here in range(i-1, j):
    basket[here] = k

print(*basket, sep=' ')