def coin_change(coins, amount):
    """Return the minimum coin count for amount, or -1 if impossible."""
    if amount < 0:
        return -1
    maximum = amount + 1
    minimum = [maximum] * (amount + 1)
    minimum[0] = 0
    for total in range(1, amount + 1):
        for coin in coins:
            if coin > 0 and coin <= total:
                minimum[total] = min(minimum[total], minimum[total - coin] + 1)
    return minimum[amount] if minimum[amount] != maximum else -1
