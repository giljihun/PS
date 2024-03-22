X = int(input())
line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    parents = X
    son = line - X + 1

else:
    parents = line - X + 1
    son = X

print(f"{parents}/{son}")