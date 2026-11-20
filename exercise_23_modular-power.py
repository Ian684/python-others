def modular_power(base, exponent, modulus):
    """Compute base ** exponent modulo modulus without overflow."""
    if modulus == 0:
        raise ValueError("modulus must be non-zero")
    if exponent < 0:
        raise ValueError("exponent must be non-negative")
    result = 1 % modulus
    base %= modulus
    while exponent:
        if exponent & 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent >>= 1
    return result
