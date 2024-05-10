a, b, c = map(int, input().split())

tri = []

tri.append(a)
tri.append(b)
tri.append(c)

tri.sort()

while sum(tri[:2]) <= tri[2]:
    tri[2] -= 1

print(sum(tri))