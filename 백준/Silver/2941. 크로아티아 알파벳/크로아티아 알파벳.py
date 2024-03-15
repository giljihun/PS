word = str(input())
answer = 0

croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for cr in croa:
    word = word.replace(cr, 'N')

print(len(word))