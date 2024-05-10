tri = []

for _ in range(3):
    tri.append(int(input()))

if tri[0] == 60 and tri[1] == 60 and tri[2] == 60:
    print("Equilateral")

else:
    if sum(tri) == 180:
        if tri[0] in tri[1:]:
            print("Isosceles")
        elif tri[1] == tri[2]:
            print("Isosceles")
        else:
            print("Scalene")

    if sum(tri) != 180:
        print("Error")