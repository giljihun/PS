# 각 인덱스에서 다음으로 갈 수 있는 칸의 번호
BoardCanMoving = [
    [1], [2], [3], [4], [5],
    [6, 21], [7], [8], [9], [10],
    [11, 25], [12], [13], [14], [15],
    [16, 27], [17], [18], [19], [20],
    [32], [22], [23], [24], [30],
    [26], [24], [28], [29], [24],
    [31], [20], [32]
]

# 각 칸 별 획득 가능 점수
board_Score = [0, 2, 4, 6, 8,
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28,
         30, 32, 34, 36, 38,
         40, 13, 16, 19, 25,
         22, 24, 28, 27, 26,
         30, 35, 0]

dice = list(map(int, input().split()))
answer = 0


def backtracking(dice_number, result, horses):
    global answer
    if dice_number == 10:
        answer = max(answer, result)
        return

    for i in range(4):
        # 현재 말 위치
        x = horses[i]

        # 현재 말 위치가 두 갈래 길인가?
        if len(BoardCanMoving[x]) == 2:
            # 파란길로 한 칸!
            x = BoardCanMoving[x][1]
        else:
            # 빨간길로 한 칸!
            x = BoardCanMoving[x][0]

        # 주사위 값만큼 말 이동(위에서 방향 전환용으로 미리 1칸 이동한 상태)
        for _ in range(1, dice[dice_number]):
            x = BoardCanMoving[x][0]

        # 목적지에 도착했거나 or (아직 목적지가 아니고 and 거기에 말이 없다면)
        if x == 32 or (x < 32 and x not in horses):
            before = horses[i]  # 이전 말의 위치
            horses[i] = x  # 현재 말 위치 갱신

            backtracking(dice_number + 1, result + board_Score[x], horses)

            horses[i] = before

backtracking(0, 0, [0, 0, 0, 0])

print(answer)