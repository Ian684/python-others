def find_mountain_peak(values):
    """Return the index of a peak in a bitonic mountain array."""
    if not values:
        raise ValueError("values must not be empty")
    low, high = 0, len(values) - 1
    while low < high:
        middle = (low + high) // 2
        if values[middle] < values[middle + 1]:
            low = middle + 1
        else:
            high = middle
    return low
