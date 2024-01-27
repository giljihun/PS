N = str(input())

answer = []
for i in N:
    answer.append(i)
    
for i in range(len(answer) - 1, -1, -1):
    print(answer[i], end='')