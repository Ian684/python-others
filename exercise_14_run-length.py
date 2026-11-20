def run_length_encode(text):
    """Encode repeated characters as (character, count) pairs."""
    if not text:
        return []
    encoded = []
    character = text[0]
    count = 1
    for current in text[1:]:
        if current == character:
            count += 1
        else:
            encoded.append((character, count))
            character, count = current, 1
    encoded.append((character, count))
    return encoded

def run_length_decode(pairs):
    """Decode (character, count) pairs into text."""
    return ''.join(character * count for character, count in pairs)
