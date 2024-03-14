N = int(input())

star = '*'
blank = ' '
cnt = 1

for i in range(N-1):
    print(blank * (N-i-1), end='')
    print(star * cnt)
    cnt += 2

cnt = N + N-1

for i in range(N-1, -1, -1):
    print(blank * (N-i-1), end='')
    print(star * cnt)
    cnt -= 2
