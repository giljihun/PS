def solution(my_string, overwrite_string, s):
    
    answer = ''
    
    answer = my_string[:s] + overwrite_string
    
    length = len(answer)
    
    answer = answer + my_string[length:]
    
    print(answer)
    
    return answer