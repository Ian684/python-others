def edit_distance(left, right):
    """Return the Levenshtein edit distance between two strings."""
    dp = list(range(len(right) + 1))
    for left_index, left_character in enumerate(left, 1):
        next_row = [left_index]
        for right_index, right_character in enumerate(right, 1):
            replacement = dp[right_index - 1] + (left_character != right_character)
            insertion = next_row[-1] + 1
            deletion = dp[right_index] + 1
            next_row.append(min(replacement, insertion, deletion))
        dp = next_row
    return dp[-1]
