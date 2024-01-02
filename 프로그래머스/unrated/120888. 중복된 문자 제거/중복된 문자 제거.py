def solution(my_string):
    answer = ''

    knew_list = []

    for alphabet in my_string:
        if alphabet in knew_list:
            pass
        else:
            knew_list.append(alphabet)
            
    for alphabet in knew_list:
        answer = str(answer) + str(alphabet)
        
    return answer