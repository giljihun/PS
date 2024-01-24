import itertools

N, M = map(int, input().split())

cards = list(map(int, input().split()))

nCr = itertools.combinations(cards, 3)

max_diff = float('inf')
answer = 0

for i in nCr:
    current_diff = abs(M - sum(i))
    if max_diff > current_diff and sum(i) <= M:
        max_diff = current_diff
        if sum(i) <= M:
            answer = sum(i)

print(answer)