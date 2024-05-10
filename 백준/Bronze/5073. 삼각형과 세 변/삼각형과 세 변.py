while(True):
    tri = []
    a, b, c = map(int, input().split())
    
    tri.append(a)
    tri.append(b)
    tri.append(c)

    if a == 0 and b == 0 and c == 0:
        break

    else:
        
        tri.sort()

        if tri[2] >= tri[0] + tri[1]:
            print("Invalid")
        
        else:
            if tri[0] == tri[1] == tri[2]:
                print("Equilateral")

            elif tri[0] in tri[1:]:
                print("Isosceles")
            
            elif tri[1] == tri[2]:
                print("Isosceles")
            
            else:
                print("Scalene")