N = int(input())
answer = 0

for _ in range(N):
    flag = False
    word = str(input())

    for i in range(len(word)):
        if len(list(set(word))) == 1:
            flag = True
            break

        elif word[i] not in word[i+1:i+2] and word[i] in word[i+2:]:
            flag = False
            break
        else:
            flag = True

    if flag == True:
        answer += 1
        flag = False

print(answer)