a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

real = []

for i in range(n0, 101):
    if (a1 * i + a0) <= (c * i):
        real.append(True)
    else:
        real.append(False)

if all(real):
    print("1")
else:
    print("0")

