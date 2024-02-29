import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

# 정렬
nums.sort()

# 산술평균
print((round(sum(nums) / N)))

# 중앙값
print((nums[len(nums)//2]))

# 최빈값
many = {}
for num in nums:
    if num in many:
        many[num] += 1
    else:
        many[num] = 1

maxy = max(many.values())
maxys = []

for i in many:
    if maxy == many[i]:
        maxys.append(i)

if len(maxys) > 1:
    print(maxys[1])
else:
    print(maxys[0])

# 범위
print(max(nums) - min(nums))