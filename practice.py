N, K = map(int, input().split())

index = 0
queue = [num for num in range(1, N+1)]
answer = []

while queue:

    index += K - 1
    if index >= len(queue):
        index %= len(queue)
    answer.append(str(queue.pop(index)))

print("<", ', '.join(answer), ">", sep="")











