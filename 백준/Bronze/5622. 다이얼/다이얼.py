# 1 -> 2초 2 -> 3초 . . .
# 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면됨.
# UNUCIC -> 868242
# 9 2 -> 13초

dial = [
    [3, 'A','B','C'],
    [4, 'D','E','F'],
    [5, 'G','H','I'],
    [6, 'J','K','L'],
    [7, 'M','N','O'],
    [8, 'P','Q','R','S'],
    [9, 'T','U','V'],
    [10, 'W','X','Y','Z'] ]

word = str(input())
time = 0
for w in word:
    for lst in dial:
        if w in lst:
            time = time + lst[0]

print(time)
