board = []

for _ in range(5):
    board.append(input())

max_length = max(len(row) for row in board)

answer = ""

for i in range(max_length):
    for j in range(5):
        if i < len(board[j]):
            answer += board[j][i]

print(answer)
