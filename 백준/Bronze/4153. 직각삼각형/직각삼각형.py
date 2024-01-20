while(True):
  triangle = []
  a, b, c = map(int, input().split())

  triangle.append(a)
  triangle.append(b)
  triangle.append(c)

  if a==0 and b==0 and c==0:
    break

  triangle = sorted(triangle)

  if ((triangle[0] ** 2) + (triangle[1] ** 2) == triangle[2] ** 2):
    print("right")
  else:
    print("wrong")