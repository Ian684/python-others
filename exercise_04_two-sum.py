def two_sum(values, target):
    """Return indices of two values that add to target, or None."""
    seen = {}
    for index, value in enumerate(values):
        other = target - value
        if other in seen:
            return [seen[other], index]
        seen[value] = index
    return None
