# N개의 바구니, 공이 한개씩 들어있음. 바구니 번호와 같은 번호의 공이 들어있음.

N, M = map(int, input().split())
basket = []
for i in range(1, N+1):
  basket.append(i)

for _ in range(M):
  i, j = map(int, input().split())

  basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)