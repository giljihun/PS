M = int(input())
N = int(input())
answer = []

for index in range(M, N+1):
    sqr = index ** (1/2)

    if int(sqr) ** 2 == index:
        answer.append(index)

if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)