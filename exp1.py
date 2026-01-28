N = 8
board = [-1] * N

def solve(col):
    if col == N:
        return True
    for row in range(N):
        if all(board[c] != row and abs(board[c] - row) != abs(c - col) for c in range(col)):
            board[col] = row
            if solve(col + 1):
                return True
    return False

solve(0)

for r in range(N):
    print(" ".join("Q" if board[c] == r else "." for c in range(N)))