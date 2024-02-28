while(True):
  sentence = input()

  # .이면 종료 
  if sentence == ".":
    break
  # 균형정보를 저장할 스택
  stack = []

  # 균형정보 가져오기
  for word in sentence:
      if word == '(' or word == '[':
          stack.append(word)
      elif  word == ')':
        if len(stack) and stack[-1] == '(':
          stack.pop()
        else:
          stack.append(word)
          break
      elif word == ']':
            if len(stack) and stack[-1]=='[': 
                stack.pop()
            else: 
                stack.append(word)
                break

  if not stack:
    print('yes')
  else:
    print('no')