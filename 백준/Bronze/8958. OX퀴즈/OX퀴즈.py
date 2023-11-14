TESTCASE_COUNT = int(input())

answer_list = []

for _ in range(TESTCASE_COUNT):
  CASE = input()
  point = 0
  result = 0
  for char in CASE:  
    if char == 'O':
      point = point + 1
      result = result + point
    else:
      point = 0
  answer_list.append(result)

for answer in answer_list:
  print(answer)