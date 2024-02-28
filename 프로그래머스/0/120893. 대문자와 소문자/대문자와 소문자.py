def solution(my_string):
    answer = ''
    for char in my_string:
        if char.islower():
            answer = answer + chr(int(ord(char)) - 32)
        else:
            answer = answer + chr(int(ord(char)) + 32)
            
    return answer