def solution(n):
    answer = 0
    
    new = sorted(str(n), reverse=True)
    
    for index in new:
        answer = str(answer) + str(index)
    
    return int(answer)