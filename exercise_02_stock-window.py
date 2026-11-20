def max_profit(prices):
    """Return the maximum profit obtainable from one buy/sell pair."""
    if not prices:
        return 0
    minimum = prices[0]
    profit = 0
    for price in prices[1:]:
        minimum = min(minimum, price)
        profit = max(profit, price - minimum)
    return profit
