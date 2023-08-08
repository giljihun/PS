import math

n = int(input())
nums = [int(input()) for _ in range(n)]

diffs = [abs(nums[i]-nums[j]) for i in range(n-1) for j in range(i+1, n)]
gcd_val = diffs[0]
for i in range(1, len(diffs)):
    gcd_val = math.gcd(gcd_val, diffs[i])

m_values = set()
for i in range(2, int(gcd_val**0.5)+1):
    if gcd_val % i == 0:
        m_values.add(i)
        m_values.add(gcd_val // i)

m_values.add(gcd_val)

m_list = sorted(list(m_values))
for m in m_list:
    print(m, end=' ')
