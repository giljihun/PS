from collections import deque
import sys

T = int(sys.stdin.readline())

answer = []

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    sig = deque(list(map(int, sys.stdin.readline().split())))
    count = 0

    while sig:
        # 현재 큐의 최대값 저장
        master = max(sig)
        # 맨 앞 값 저장 및 pop
        front = sig.popleft()
        # 내가 원하는 녀석의 위치가 한 칸 앞으로
        M -= 1

        # 근데 맨 앞이 마스터다?
        if master == front:
            count += 1
            # m이 0이다? 내 숫자가 맨 앞이었다는 것.
            if M < 0:
                answer.append(count)
                break

        else:
            sig.append(front)
            if M < 0:
                M = len(sig) - 1

print(*answer, sep='\n')