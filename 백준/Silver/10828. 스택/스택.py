# boj10828 스택

stack = []
output = []

for _ in range(int(input())):
  command = input().split()

  # push 출력 x
  if command[0] == "push":
    stack.append(command[1])

  elif command[0] == "pop":
    if stack:
      output.append(stack.pop())
    else:
      output.append(-1)

  elif command[0] == "size":
    output.append(len(stack))

  elif command[0] == "empty":
    if stack:
      output.append(0)
    else:
      output.append(1)

  elif command[0] == "top":
    if stack:
      output.append(stack[-1])
    else:
      output.append(-1)

for cmd in output:
  print(cmd)