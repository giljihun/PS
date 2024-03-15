word = str(input())
mid = len(word) // 2
forward = []
backward = []
# 홀수
if len(word) % 2 == 1:
    for wd in word[:mid]:
        forward.append(wd)

    for wd in word[mid+1:]:
        backward.append(wd)
    backward.reverse()

else:
    for wd in word[:mid]:
        forward.append(wd)

    for wd in word[mid:]:
        backward.append(wd)
    backward.reverse()

if forward == backward:
    print(1)
else:
    print(0)