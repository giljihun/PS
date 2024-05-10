x = []
y = []
N = int(input())

for _ in range(N):
    a, b = map(int ,input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

print((x[-1] - x[0]) * (y[-1] - y[0]))