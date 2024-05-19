N = int(input())
myCards = list(map(int, input().split()))
myCards.sort()

M = int(input())
targetCards = list(map(int ,input().split()))

answer = []

# 이진탐색 
# -> 타겟을 미드값과 비교해서 미드값보다 작으면 왼쪽
# 크면 오른쪽으로.
# 이동한 곳에서 또 미드값과 비교.

def searchCard(myDeck, targetCard, start, end):
    if start > end:
        answer.append(0)
        return 
    
    mid = (start + end) // 2

    if targetCard == myDeck[mid]:
        answer.append(1)
        return
    
    elif targetCard < myDeck[mid]:
        return searchCard(myDeck, targetCard, start, mid-1)

    else:
        return searchCard(myDeck, targetCard, mid+1, end)
    

for target in targetCards:
    searchCard(myCards, target, 0, len(myCards) - 1)
    #print(answer)

print(*answer)