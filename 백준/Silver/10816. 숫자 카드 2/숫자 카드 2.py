import sys

N = sys.stdin.readline()
my_cards = list(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline()
target_cards = list(map(int, sys.stdin.readline().split()))

dic = {}

for x in my_cards:
  if x in dic :
    dic[x] += 1
  else:
    dic[x] = 1

for x in target_cards:
  if x in dic:
    print(dic[x], end=' ')
  else:
    print('0', end= ' ')