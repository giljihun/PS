def solution(n):
    answer = []
    
    target = str(n)
    
    for i in range(len(target), 0, -1):
        
        answer.append(int(target[i-1]))
        
    return answer