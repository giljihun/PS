a = int(input())

stk = []

for _ in range(a):
  num = int(input())
  if num == 0:
    stk.pop()

  else:
    stk.append(num)

print(sum(stk))