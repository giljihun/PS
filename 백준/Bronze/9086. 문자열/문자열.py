T = int(input())
ans = []
for _ in range(T):
    sen = input()
    st = sen[0]
    ed = sen[-1]
    ans.append(st+ed)
    
for a in ans:
    print(a)
    