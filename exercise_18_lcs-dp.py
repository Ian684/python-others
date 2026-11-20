def longest_common_subsequence(left, right):
    """Return the length of a longest common subsequence."""
    dp = [0] * (len(right) + 1)
    for left_item in left:
        previous = 0
        for column, right_item in enumerate(right, 1):
            saved = dp[column]
            if left_item == right_item:
                dp[column] = previous + 1
            else:
                dp[column] = max(dp[column], dp[column - 1])
            previous = saved
    return dp[-1]
