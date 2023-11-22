N = int(input())

subjects = list(map(int, input().split()))

mx = max(subjects)
sum = 0

for i in range(N):
  subjects[i] = subjects[i] / float(mx) * 100
  sum += subjects[i]

print(sum / N)