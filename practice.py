import sys

T = int(sys.stdin.readline())
answer = []

for _ in range(T):
    stack = []
    s = input()
    VPS = True

    for ch in s:
        if ch == '(':
            stack.append('(')
        if ch == ')':
            if stack:
                stack.pop()
            elif not stack:
                VPS = False
                break

    if not stack and VPS:
        answer.append("YES")
    elif stack or not VPS:
        answer.append("NO")

for ans in answer:
   print(ans)



