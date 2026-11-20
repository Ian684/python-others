def longest_palindrome(text):
    """Return one longest palindromic substring."""
    if not text:
        return ''
    start = end = 0
    for center in range(len(text)):
        for left, right in ((center, center), (center, center + 1)):
            while left >= 0 and right < len(text) and text[left] == text[right]:
                if right - left > end - start:
                    start, end = left, right
                left -= 1
                right += 1
    return text[start:end + 1]
