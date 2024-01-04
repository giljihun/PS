def solution(before, after):
    answer = 0
    
    # 만약 문자열 길이가 다르다? 그럼 그냥 당연히 못만듬.
    if len(before) != len(after):
        pass
    
    # 알파벳 개수를 세서 개수가 일치하면 만들 수 있다.
    else:
        
        counting_before = {}
        counting_after = {}
        
        for i in range(len(before)):
            if before[i] in counting_before:
                counting_before[before[i]] += 1
                
            else:
                counting_before[before[i]] = 1
            
        for i in range(len(after)):
            if after[i] in counting_after:
                counting_after[after[i]] += 1
                
            else:
                counting_after[after[i]] = 1
    
    if counting_before == counting_after:
        answer = 1
        
    else:
        answer = 0
    
    return answer

# def solution(before, after):
#     before=sorted(before)
#     after=sorted(after)
#     if before==after:
#         return 1
#     else:
#         return 0