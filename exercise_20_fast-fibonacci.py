def fibonacci(number):
    """Return Fibonacci(number) using fast doubling."""
    if number < 0:
        raise ValueError("number must be non-negative")
    def calculate(n):
        if n == 0:
            return 0, 1
        a, b = calculate(n // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        return (d, c + d) if n % 2 else (c, d)
    return calculate(number)[0]
