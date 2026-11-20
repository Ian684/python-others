def knapsack(values, weights, capacity):
    """Return the maximum value within capacity using 0/1 items."""
    if len(values) != len(weights):
        raise ValueError("values and weights must have the same length")
    if capacity < 0:
        raise ValueError("capacity must be non-negative")
    dp = [0] * (capacity + 1)
    for value, weight in zip(values, weights):
        if weight < 0:
            raise ValueError("weights must be non-negative")
        for remaining in range(capacity, weight - 1, -1):
            dp[remaining] = max(dp[remaining], dp[remaining - weight] + value)
    return dp[capacity]
