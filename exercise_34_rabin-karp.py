def rabin_karp(text, pattern):
    """Return start indices of pattern occurrences using rolling hashes."""
    if not pattern:
        return list(range(len(text) + 1))
    if len(pattern) > len(text):
        return []
    base = 257
    modulus = 1_000_000_007
    pattern_hash = 0
    window_hash = 0
    highest_place = 1
    for _ in range(len(pattern) - 1):
        highest_place = highest_place * base % modulus
    for character in pattern:
        pattern_hash = (pattern_hash * base + ord(character)) % modulus
    for character in text[:len(pattern)]:
        window_hash = (window_hash * base + ord(character)) % modulus
    matches = []
    for start in range(len(text) - len(pattern) + 1):
        if window_hash == pattern_hash and text[start:start + len(pattern)] == pattern:
            matches.append(start)
        if start < len(text) - len(pattern):
            outgoing = ord(text[start]) * highest_place % modulus
            incoming = ord(text[start + len(pattern)])
            window_hash = (window_hash - outgoing) % modulus
            window_hash = (window_hash * base + incoming) % modulus
    return matches
