def prefix_sums(values):
    """Return cumulative sums, including zero before the first value."""
    result = [0]
    total = 0
    for value in values:
        total += value
        result.append(total)
    return result

def range_sum(prefix, left, right):
    """Return the inclusive sum for [left, right] using prefix_sums output."""
    if left < 0 or right < left or right >= len(prefix) - 1:
        raise IndexError("range is outside the input")
    return prefix[right + 1] - prefix[left]
