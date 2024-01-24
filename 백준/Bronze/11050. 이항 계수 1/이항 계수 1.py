import itertools

N, K = map(int, input().split())
temp = []

for _ in range(N):
    temp.append('*')

nCk = list(itertools.combinations(temp, K))

print(len(nCk))