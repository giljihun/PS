# 벌집

N = int(input())

cnt = 0
scale = 1

if N == 0:
    print("1")
else:
    while(True):
        if N <= 0:
            print(cnt)
            break

        N = N - scale
        cnt += 1
        scale = 6 * cnt