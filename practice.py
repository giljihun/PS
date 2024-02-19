# import sys

# N = sys.stdin.readline()
# my_cards = list(map(int, sys.stdin.readline().split()))
# M = sys.stdin.readline()
# target_cards = list(map(int, sys.stdin.readline().split()))
# answer = []

# for i in range(len(target_cards)):
#     cnt = 0
#     for j in range(len(my_cards)):
#         if target_cards[i] == my_cards[j]:
#             cnt += 1
#     answer.append(cnt)

# for ans in answer:
#     print(ans, end=' ')

################################################

import sys

N = sys.stdin.readline()
my_cards = list(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline()
target_cards = list(map(int, sys.stdin.readline().split()))
answer = []
        
for i in range(len(target_cards)):
    answer.append(my_cards.count(target_cards[i]))

for ans in answer:
    print(ans, end=' ')