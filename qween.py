import pprint

def isSafe(board, x, y, n):
    # Check column
    for row in range(x):
        if board[row][y] == 'Q':
            return False

    # Check top-left diagonal
    row, col = x, y
    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    # Check top-right diagonal
    row, col = x, y
    while row >= 0 and col < n:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col += 1

    return True

def nQueen(board, x, n):
    if x >= n:
        return True

    for col in range(n):
        if isSafe(board, x, col, n):
            board[x][col] = 'Q'
            if nQueen(board, x+1, n):
                return True
            board[x][col] = ' '  # backtrack
    return False

n = int(input("Enter number of Q: "))
board = [[' ']*n for _ in range(n)]
if nQueen(board, 0, n):
    pprint.pprint(board)
else:
    print("No Solution")
