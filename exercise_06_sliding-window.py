def max_subarray_sum(values, size):
    """Return the largest sum in a contiguous window of the given size."""
    if size <= 0:
        raise ValueError("size must be positive")
    if size > len(values):
        raise ValueError("size exceeds the number of values")
    window = sum(values[:size])
    maximum = window
    for index in range(size, len(values)):
        window += values[index] - values[index - size]
        maximum = max(maximum, window)
    return maximum
