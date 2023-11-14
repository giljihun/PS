SIG_NUM = list(map(int, input().split()))

SUM = 0

for NUM in SIG_NUM:
  SUM += NUM ** 2

print(SUM % 10)