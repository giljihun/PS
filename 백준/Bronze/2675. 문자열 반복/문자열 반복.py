T = int(input())

i = 0
P = [''] * T

for _ in range(T):
    R, S = input().split()
    R = int(R)   

    for char in S:
        P[i] += char * R
    i = i + 1    

for result in P:
  print(result)
