n = int(input())

lst = list(map(int, input().split()))

dp = [0] * n
dp[0] = lst[0]

for i in range(0, n-1):

    dp[i+1] = max(lst[i+1], dp[i] + lst[i+1])

print(max(dp))
