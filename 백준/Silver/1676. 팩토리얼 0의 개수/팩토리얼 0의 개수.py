N = int(input())
cnt = 0
fact = 1

for num in range(N, 1, -1):
    fact = fact * num
    
fact = str(fact)

for num in range(len(fact)-1, -1, -1):
    if fact[num] == '0':
        cnt += 1
    else:
        break
print(cnt)

