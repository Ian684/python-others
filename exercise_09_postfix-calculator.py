import operator

_OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def evaluate_postfix(tokens):
    """Evaluate a reverse Polish notation expression."""
    stack = []
    for token in tokens:
        if token in _OPERATORS:
            if len(stack) < 2:
                raise ValueError("invalid postfix expression")
            right = stack.pop()
            left = stack.pop()
            if token == '/' and right == 0:
                raise ZeroDivisionError("division by zero")
            stack.append(_OPERATORS[token](left, right))
        else:
            try:
                stack.append(float(token) if '.' in str(token) else int(token))
            except (TypeError, ValueError) as error:
                raise ValueError("invalid postfix token") from error
    if len(stack) != 1:
        raise ValueError("invalid postfix expression")
    return stack[0]
