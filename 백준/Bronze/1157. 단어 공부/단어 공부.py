word = input()

wordlength = len(word)

dic_word = {}

for i in range(wordlength):
    if word[i].upper() not in dic_word:
        dic_word[word[i].upper()] = 1
    else:
        dic_word[word[i].upper()] += 1
        
max_value = max(dic_word.values())

max_keys = [key for key, value in dic_word.items() if value == max_value]

if len(max_keys) == 1:
    print(max_keys[0].upper())
else:
    print('?')
