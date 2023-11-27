N = int(input())

if N % 2 == 1:
    print("long", end=" ")
    for _ in range((N // 4)):
        print("long ", end="")
    print("int")

else:
    for _ in range((N // 4)):
        print("long ", end="")
    print("int")

