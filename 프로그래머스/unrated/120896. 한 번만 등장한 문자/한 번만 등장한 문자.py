def solution(s):
    answer = ''
    
    every_lst = []
    only_lst = []
    
    for alphabet in s:
        every_lst.append(alphabet)
        
    for i in every_lst:
        if every_lst.count(i) == 1:
            only_lst.append(i)
            
    only_lst.sort()
    
    for index in only_lst:
        answer = str(answer) + str(index)
        
    return answer