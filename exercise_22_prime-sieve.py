def prime_sieve(limit):
    """Return all primes no greater than limit."""
    if limit < 2:
        return []
    is_prime = bytearray(b'\x01') * (limit + 1)
    is_prime[0:2] = b'\x00\x00'
    for divisor in range(2, int(limit ** 0.5) + 1):
        if is_prime[divisor]:
            is_prime[divisor * divisor:limit + 1:divisor] = b'\x00' * (((limit - divisor * divisor) // divisor) + 1)
    return [number for number in range(limit + 1) if is_prime[number]]
