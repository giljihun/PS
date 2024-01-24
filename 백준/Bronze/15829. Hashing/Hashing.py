L = int(input())
stc = list(map(str, input().split()))

answer = 0

for i in range(0, L):
    convert_aschii = (ord(str(stc[0][i])) - 96)

    answer = answer + (convert_aschii * (31 ** i))

print(answer)