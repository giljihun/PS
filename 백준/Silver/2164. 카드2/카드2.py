import sys
from collections import deque

N = int(sys.stdin.readline())

# N이 만약 6이다, [1, 2, 3, 4, 5, 6] 이렇게 됨.

# 동작 : 맨위([0])를 pop한다. -> 그 다음 맨위를 맨 뒤로 옮긴다 (pop, append)

deck = []
for num in range(1, N+1):
    deck.append(num)
deck = deque(deck)

while(len(deck) != 1):
    # 동작1
    deck.popleft()
    # 동작2
    deck.rotate(-1)

print(deck[0])
