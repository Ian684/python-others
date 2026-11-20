def spiral_matrix(size):
    """Create an n x n matrix filled clockwise with consecutive integers."""
    if size < 0:
        raise ValueError("size must be non-negative")
    result = [[0] * size for _ in range(size)]
    top, bottom, left, right = 0, size - 1, 0, size - 1
    number = 1
    while top <= bottom and left <= right:
        for column in range(left, right + 1):
            result[top][column] = number
            number += 1
        top += 1
        for row in range(top, bottom + 1):
            result[row][right] = number
            number += 1
        right -= 1
        if top <= bottom:
            for column in range(right, left - 1, -1):
                result[bottom][column] = number
                number += 1
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result[row][left] = number
                number += 1
            left += 1
    return result
