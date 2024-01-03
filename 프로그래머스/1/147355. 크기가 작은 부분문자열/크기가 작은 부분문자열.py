def solution(t, p):
    answer = 0
    
    # p의 길이가 3이라면 
    # 0 1 2 / 1 2 3 / 2 3 4 / 3 4 5 ... 이런식으로 읽으면 됨.
    
    start = 0
    end = len(p)
    
    while(end != len(t) + 1):
        if int(t[start:end]) <= int(p):
            answer += 1
        
        start += 1
        end += 1
    
    return answer