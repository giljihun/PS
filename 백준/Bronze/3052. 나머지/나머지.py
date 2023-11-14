num_list = [0] * 10

for i in range(10):
  number = int(input())
  number = number % 42 
  num_list[i] = number

num_list = set(num_list)

print(len(num_list))