x = []
y = []
target_x = 0
target_y = 0

for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

if x[0] in x[1:]:
    if x[0] == x[1]:
        target_x = x[2]
    else:
        target_x = x[1]

else:
    target_x = x[0]

if y[0] in y[1:]:
    if y[0] == y[1]:
        target_y = y[2]
    else:
        target_y = y[1]
else:
    target_y = y[0]

print(target_x, target_y)