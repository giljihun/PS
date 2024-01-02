def solution(q, r, code):
    
    answer = ''
    
    for i in range(len(code)):
            
        if i % q == r:
            answer = answer + str(code[i])
                
    return answer