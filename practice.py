# a층의 b호에 살려면..
# 아래층(a-1)의 1호부터 b호
# 까지 사람들 수의 합만큼
# 사람들을 데려와 살아야 한다?

# k층 n호엔 몇 명이 사는가?!
# 조건1. 0층, 1호부터 있음.
# 조건2. 0층 i호에는 i명이 산다.

# 3층 1명, 5명, 15명, 35명
# 2층 1명, 4명, 10명, 20명
# 1층 1명, 3명, 6명, 10명
# 0층 1명, 2명, 3명, 4명

# k=2, n=3 -> 10
T = int(input())
answer = []
while T != 0:
    T -= 1
    k = int(input())
    n = int(input())

    if n == 1:
        answer.append(1)

    else:
        for i in range(k):








if T == 0:
    for ans in answer:
        print(ans)

