T = int(input())
answer = []

while(T > 0):
  C = int(input())
  charge = [0, 0, 0 ,0]

  if C // 25 > 0:
    charge[0] = C // 25
    C = C % 25
  
  if C // 10 > 0:
    charge[1] = C // 10
    C = C % 10
    
  if C // 5 > 0:
    charge[2] = C // 5
    C = C % 5

  charge[3] = C

  answer.append(charge)
  
  T -= 1

for i in range(len(answer)):
  print(*answer[i])