import math
import random
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def evaluate(board):
    # Check rows
    for row in board:
        if row.count('X') == 3:
            return 10
        elif row.count('O') == 3:
            return -10

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == 'X':
            return 10
        elif board[0][col] == board[1][col] == board[2][col] == 'O':
            return -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
        return 10
    elif board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        return -10

    # If no winner yet
    return 0

def is_moves_left(board):
    for row in board:
        for cell in row:
            if cell == '_':
                return True
    return False

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = '_'
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = '_'
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = '_'

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

def main():
    board = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]

    print("Initial Board:")
    print_board(board)

    while True:
        # player_move = input("Enter your move (row col): ").split()
        valid_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    valid_moves.append((i, j))
        
        row, col = random.choice(valid_moves)
        print("Random Player's move:")
        print_board(board)

        if evaluate(board) == -10:
            print("You Win!")
            break
        elif not is_moves_left(board):
            print("It's a draw!")
            break

        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print("AI's move:")
        print_board(board)

        if evaluate(board) == 10:
            print("AI Wins!")
            break
        elif not is_moves_left(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
