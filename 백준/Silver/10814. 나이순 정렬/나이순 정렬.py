# boj 10814 , 나이순 정렬
# 240129

N = int(input())
people = []

for i in range(N):
    age, name = input().split()
    age = int(age)
    name = str(name)
    people.append((age, name))

people.sort(key = lambda x:x[0])

for i in range(len(people)):
    print(people[i][0], people[i][1])