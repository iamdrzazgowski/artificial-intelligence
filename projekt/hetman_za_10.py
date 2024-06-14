def is_safe(board, row, col, n):
    # Sprawdzenie kolumny
    for i in range(n):
        if board[i][col] == 1:
            return False

    # Sprawdzenie lewej górnej przekątnej
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Sprawdzenie prawej górnej przekątnej
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    # Sprawdzenie lewej dolnej przekątnej
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Sprawdzenie prawej dolnej przekątnej
    for i, j in zip(range(row, n), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, row, n, initial_row):
    if row >= n:
        return True

    if row == initial_row:
        return solve_n_queens(board, row + 1, n, initial_row)

    for col in range(n):
        if board[row][col] == 1:
            continue

        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n, initial_row):
                return True
            board[row][col] = 0

    return False


def print_solution(board):
    index = 1
    print(" " + " A B C D E F G H")
    for row in board:
        print(f'{index} ', end="")
        print(' '.join('Q' if cell == 1 else '.' for cell in row))
        index += 1
    print()


n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

initial_position = input("Podaj początkową pozycję hetmana (np. 'B7'): ")
col_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
row = int(initial_position[1]) - 1
col = col_map.get(initial_position[0])

board[row][col] = 1

if solve_n_queens(board, 0, n, row):
    print_solution(board)
else:
    print("Nie można rozwiązać problemu z początkową pozycją hetmana.")
