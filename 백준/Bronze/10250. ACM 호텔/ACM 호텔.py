T = int(input())
answer = []

for _ in range(T):
    H, W, N = map(int, input().split())
    
    # 호텔 층(floor) 계산
    floor = N % H if N % H != 0 else H
    # 호텔 방(room) 계산
    room = (N - 1) // H + 1

    # 방 번호 계산
    room_number = floor * 100 + room
    
    answer.append(room_number)

for ans in answer:
    print(ans)
