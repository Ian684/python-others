def permutations(values):
    """Return every distinct permutation of values, preserving no duplicates."""
    ordered = list(values)
    result = []
    def generate(index):
        if index == len(ordered):
            result.append(tuple(ordered))
            return
        seen = set()
        for position in range(index, len(ordered)):
            item = ordered[position]
            if item in seen:
                continue
            seen.add(item)
            ordered[index], ordered[position] = ordered[position], ordered[index]
            generate(index + 1)
            ordered[index], ordered[position] = ordered[position], ordered[index]
    generate(0)
    return [list(permutation) for permutation in result]
