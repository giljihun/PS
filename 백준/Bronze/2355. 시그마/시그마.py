# 1~100까지는 5050. 101/2*(100)

A, B = map(int, input().split())

if A > B:
    A, B = B, A

print(int(((A+B)/2) * (B-A+1)))