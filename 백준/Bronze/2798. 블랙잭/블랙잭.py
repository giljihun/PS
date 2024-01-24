import itertools

N, M = map(int, input().split())
cards = list(map(int, input().split()))

min_diff = float('inf')
answer = 0

for combination in itertools.combinations(cards, 3):
    current_sum = sum(combination)
    current_diff = abs(M - current_sum)

    if current_diff < min_diff and current_sum <= M:
        min_diff = current_diff
        answer = current_sum

print(answer)
