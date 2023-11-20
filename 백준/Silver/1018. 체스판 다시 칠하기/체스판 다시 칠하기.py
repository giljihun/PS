M, N = map(int, input().split())
board = []

for _ in range(M):
    row = list(input())
    board.append(row)

min_changes = float('inf')

for i in range(M - 7):
    for j in range(N - 7):
        # 시작점이 'B'로 시작하는 경우
        changes_B = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:  # 흰 칸일 때
                    if board[x][y] != 'W':
                        changes_B += 1
                else:  # 검은 칸일 때
                    if board[x][y] != 'B':
                        changes_B += 1

        # 시작점이 'W'로 시작하는 경우
        changes_W = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:  # 흰 칸일 때
                    if board[x][y] != 'B':
                        changes_W += 1
                else:  # 검은 칸일 때
                    if board[x][y] != 'W':
                        changes_W += 1

        min_changes = min(min_changes, changes_B, changes_W)

print(min_changes)
