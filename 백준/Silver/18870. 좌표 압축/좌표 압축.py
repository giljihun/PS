N = int(input())
num = list(map(int, input().split()))

# 중복제거
noDup = sorted(set(num))

# enumerate(noDup) -> -10 : 0, -0 : 1 ...
index_map = {value: index for index, value in enumerate(noDup)}

answer = [index_map[value] for value in num]
print(*answer)
