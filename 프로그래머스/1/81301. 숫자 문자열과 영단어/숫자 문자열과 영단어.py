def solution(s):
    answer = ''
    
    ENG = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight': 8, 'nine' : 9}
    what = ''
    
    # 영어가 나오다가 숫자가 나오면 거기서 끊,
    # 숫자가 나오다가 영어가 나오면 거기서 끊. 어야하는데. --> 어떻게 끊어야할까?
    
    # 1. 인덱스를 하나하나 탐색한다.
    for index in s:
        # 2. 만약 숫자다? 그럼 answer에 추가.
        if index.isdecimal():
            answer = str(answer) + str(index)
            
        # 3. 문자열이다? 그러면 판별 리스트에 넣어보자.
        else:
            what = what + index
            if what in ENG:
                answer = str(answer) + str(ENG[what])
                what = ''
    
    return int(answer)