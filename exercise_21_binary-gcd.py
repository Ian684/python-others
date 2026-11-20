def binary_gcd(left, right):
    """Return the greatest common divisor using the binary algorithm."""
    left, right = abs(left), abs(right)
    if left == 0:
        return right
    if right == 0:
        return left
    shift = 0
    while ((left | right) & 1) == 0:
        left >>= 1
        right >>= 1
        shift += 1
    while (left & 1) == 0:
        left >>= 1
    while right:
        while (right & 1) == 0:
            right >>= 1
        if left > right:
            left, right = right, left
        right -= left
    return left << shift
