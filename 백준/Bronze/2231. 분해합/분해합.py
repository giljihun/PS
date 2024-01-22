# 분해합
# 245 => 245 + 2 + 4 + 5 = 256
# N이 주어졌을 때 가장 작은 생성자 찾기
# 216 => 198 (198 + 1 + 9 + 8)

N = int(input())

for i in range(1, N+1):
    partition_sum = sum(map(int, str(i)))
    entire_sum = partition_sum + i

    if entire_sum == N:
        print(i)
        break
    if i == N:
        print(0)


