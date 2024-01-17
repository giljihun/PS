import sys
input = sys.stdin.readline

#1~100까지는 5500. 100/2*(100+1)
A, B = map(int, input().split())
if A > B:
    A, B = B, A
print((B-A+1)*(A+B)//2)