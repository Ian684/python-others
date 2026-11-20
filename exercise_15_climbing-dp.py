def climbing_stairs(steps):
    """Count ways to climb steps using moves of one or two."""
    if steps < 0:
        raise ValueError("steps must be non-negative")
    if steps < 2:
        return 1
    previous, current = 1, 1
    for _ in range(2, steps + 1):
        previous, current = current, previous + current
    return current
