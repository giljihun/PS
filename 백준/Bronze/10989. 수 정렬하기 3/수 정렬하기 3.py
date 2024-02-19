import sys

input = sys.stdin.readline

# 계수정렬
n = int(input())
# 입력값이 10000개까지 주어지니 10000 + 1개의 리스트
arr = [0] * (10000 + 1)  

# 각 입력값에 해당하는 인덱스의 값 +
for _ in range(n):
  arr[int(input())] += 1

# arr에 각 숫자에 해당하는 인덱스값이 생겨있음.
# 예를들어 1번 인덱스에 1이 총 2번 나왔기 때문에 
# 2가 들어가 있음.
# 그래서 1 1 이렇게 출력이 된다.
for i in range(len(arr)):
  if arr[i] != 0: 
    for _ in range(arr[i]):
      print(i)