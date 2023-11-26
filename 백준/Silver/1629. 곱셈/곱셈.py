def DAC(a, b, c):

    if b == 1:
        return a % c

    if b % 2 == 0:
        return (DAC(a, b // 2, c) ** 2) % c
    else:
        return ((DAC(a, b // 2, c) ** 2) * a) % c

a, b, c = map(int, input().split())

print(DAC(a, b, c))