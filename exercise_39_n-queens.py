def solve_n_queens(size):
    """Return all valid queen placements for an n x n board."""
    if size < 0:
        raise ValueError("size must be non-negative")
    solutions = []
    columns = set()
    descending = set()
    ascending = set()
    board = [['.' for _ in range(size)] for _ in range(size)]
    def place(row):
        if row == size:
            solutions.append([''.join(line) for line in board])
            return
        for column in range(size):
            if column in columns or row - column in descending or row + column in ascending:
                continue
            columns.add(column)
            descending.add(row - column)
            ascending.add(row + column)
            board[row][column] = 'Q'
            place(row + 1)
            board[row][column] = '.'
            columns.remove(column)
            descending.remove(row - column)
            ascending.remove(row + column)
    place(0)
    return solutions
