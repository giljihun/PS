N, M = map(int, input().split())

A = []
B = []

for _ in range(N):
  A.append(list(map(int,input().split())))

for _ in range(N):
  B.append(list(map(int,input().split())))

for i in range(len(A)):
  for j in range(len(A[0])):
    A[i][j] = A[i][j] + B[i][j]

for i in range(len(A)):
  print(*A[i])