# 소수 찾기

N = int(input())

nums = list(map(int, input().split()))
gotcha = []

for num in nums:

    if num < 2:
        continue

    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        gotcha.append(num)

print(len(gotcha))
