answer = []

for i in range(int(input())):

    k = int(input())
    n = int(input())

    # 0층에 호수만큼 생성
    apart = [[i for i in range(1, n+1)]]
    # 층수만큼 1호실에 1 넣기
    for _ in range(k):
        apart.append([1 for floor in range(n)])

    # 각 호실의 인원 넣기 wtih DP
    for i in range(1, len(apart)):
        for j in range(1, len(apart[i])):
            apart[i][j] = apart[i-1][j] + apart[i][j-1]

    answer.append(apart[-1][-1])

for ans in answer:
    print(ans)