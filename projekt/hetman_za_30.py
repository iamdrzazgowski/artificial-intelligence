def is_safe(board, row, col, n):
    # Sprawdzenie wiersza po lewej stronie
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Sprawdzenie prawej strony
    for i in range(col + 1, n):
        if board[row][i] == 1:
            return False

    # Sprawdzenie lewej górnej przekątnej
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Sprawdzenie prawej górnej przekątnej
    for i, j in zip(range(row, -1, -1), range(col + 1, n)):
        if board[i][j] == 1:
            return False

    # Sprawdzenie lewej dolnej przekątnej
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False


    # Sprawdzenie prawej dolnej przekątnej
    for i, j in zip(range(row, n), range(col + 1, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col):
    if col >= len(board):
        return [list(map(lambda row: row.index(1) + 1, board))]

    solutions = []
    for i in range(len(board)):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solutions += solve_n_queens(board, col + 1)
            board[i][col] = 0

    return solutions

def print_solutions(solutions):
    for solution in solutions:
        # print(solution)
        size = len(solution)

        board = [['.' for _ in range(size)] for _ in range(size)]

        for row, col in enumerate(solution):
            board[row][col - 1] = 'Q'

        for row in board:
            print(" ".join(row))

        print()


n = 8
board = [[0] * n for _ in range(n)]
solutions = solve_n_queens(board, 0)
print(f"Liczba rozwiązań: {len(solutions)}")
print_solutions(solutions)

