from collections import Counter

def frequency_table(values):
    """Return counts for each distinct value in insertion order."""
    counts = Counter(values)
    return dict(counts)
