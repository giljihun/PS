# boj 1065

N = int(input())
ans = 0

while(N != 0):
  flag = True
  a = []
  for num in str(N):
    a.append(int(num))

  if N < 10:
    flag = True
    ans += 1
    pass

  else:
    diff = a[1] - a[0]

    for i in range(1, len(a)):
      if diff != (a[i] - a[i-1]):
        flag = False
    
    if flag == True:
      ans += 1

  N -= 1

print(ans)
