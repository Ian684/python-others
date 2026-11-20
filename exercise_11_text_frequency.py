from collections import Counter
def solve(text):
    return dict(Counter(text.lower().split()))
