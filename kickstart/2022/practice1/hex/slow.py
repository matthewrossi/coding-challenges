DIRS = [
    (0, -1),    # left
    (-1, 0),    # top-left
    (-1, 1),    # top-right
    (0, 1),     # right
    (1, 0),     # bottom-right
    (1, -1),    # bottom-left
]


def count_moves(board, n):
    blues = reds = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'B':
                blues += 1
            elif board[i][j] == 'R':
                reds += 1
    return blues, reds


def flood(board, n, player, checked, i, j):
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        checked[i][j] = True
        for di, dj in DIRS:
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < n and 0 <= new_j < n and \
                    board[new_i][new_j] == player and \
                    not checked[new_i][new_j]:
                stack.append((new_i, new_j))


def get_winner(board, n):  
    checked = [[False] * n for _ in range(n)]
    for i in range(n):
        if board[i][0] == 'B':
            flood(board, n, 'B', checked, i, 0)
        if board[0][i] =='R':
            flood(board, n, 'R', checked, 0, i)

    for i in range(n):
        if board[i][n - 1] == 'B' and checked[i][n - 1]:
            return 'B'
        if board[n - 1][i] =='R' and checked[n - 1][i]:
            return 'R'
    return '.'
    

def solve(board, n):
    nof_blues, nof_reds = count_moves(board, n)
    if abs(nof_blues - nof_reds) > 1:
        return "Impossible"

    winner = get_winner(board, n)    
    if winner == '.':
        return "Nobody wins"
    if winner == 'B' and nof_blues < nof_reds or \
            winner == 'R' and nof_reds < nof_blues:
        return "Impossible"
    
    # Check if a winning path exists even with the removal of a stone
    for i in range(n):
        for j in range(n):
            if board[i][j] == winner:
                board[i][j] = '.'
                if get_winner(board, n) == '.':
                    return 'Blue wins' if winner == 'B' else 'Red wins'
                board[i][j] = winner
    return "Impossible"
    

if __name__ == "__main__":
    nof_tests = int(input())
    for test in range(1, nof_tests + 1):
        n = int(input())
        board = [list(input()) for _ in range(n)]
        res = solve(board, n)
        print("Case #{}: {}".format(test, res))
