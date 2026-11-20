def is_balanced(expression):
    """Return whether brackets in expression are correctly paired."""
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for character in expression:
        if character in '([{':
            stack.append(character)
        elif character in pairs:
            if not stack or stack.pop() != pairs[character]:
                return False
    return not stack
