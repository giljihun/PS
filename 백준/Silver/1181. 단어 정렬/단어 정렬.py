N = int(input())

words = []

for _ in range(N):
    word = str(input())
    words.append(word)

words = list(set(words))
words.sort()
words.sort(key=len)

for word in words:
    print(word)