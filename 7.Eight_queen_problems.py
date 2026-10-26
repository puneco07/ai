# 8-Queens Problem using Backtracking

N = 8

# Board (0 = empty, 1 = queen)
board = [[0] * N for _ in range(N)]

# Check if placing a queen is safe
def is_safe(board, row, col):

    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Backtracking function
def solve(board, row):

    # All queens are placed
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):

            # Place queen
            board[row][col] = 1

            # Solve for the next row
            if solve(board, row + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False

# Solve the problem
if solve(board, 0):
    print("Solution:")
    for row in board:
        print(*row)

    print("\nQueen positions (row, column):")
    for r in range(N):
        print((r + 1, board[r].index(1) + 1))
else:
    print("No solution exists")