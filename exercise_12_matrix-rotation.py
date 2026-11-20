def rotate_matrix_clockwise(matrix):
    """Return a new square matrix rotated 90 degrees clockwise."""
    if not matrix:
        return []
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    return [list(row) for row in zip(*matrix[::-1])]
