def merge_intervals(intervals):
    """Merge overlapping inclusive intervals and preserve their start order."""
    if not intervals:
        return []
    ordered = sorted((start, end) for start, end in intervals)
    merged = [list(ordered[0])]
    for start, end in ordered[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
