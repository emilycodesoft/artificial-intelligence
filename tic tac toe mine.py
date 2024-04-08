board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        board[i][j] = '-'

valid_moves = []
for i in range(3):
    for j in range(3):
        if board[i][j] == '_':
            valid_moves.append((i, j))