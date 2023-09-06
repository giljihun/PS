import math

def solution(fees, records):
    answer = []
    inTime = [0] * 10000
    isIn = [0] * 10000
    sumT = [0] * 10000
    
    for record in records:
        time, car_num, IO = record.split()
        h, m = time.split(":")
        
        if IO == 'IN':
            inTime[int(car_num)] = int(h) * 60 + int(m )
            isIn[int(car_num)] = 1
        else:
            sumT[int(car_num)] += (int(h) * 60 + int(m)) - inTime[int(car_num)]
            isIn[int(car_num)] = 0
            
    for i in range(10000):
        if isIn[i] == 1:
            sumT[i] += (23 * 60 + 59) - inTime[i]
            
            
    for i in range(10000):
        if sumT[i] > 0:
            answer.append(fees[1] + max(math.ceil((sumT[i] - fees[0])/fees[2]), 0) * fees[3])
        
    return answer