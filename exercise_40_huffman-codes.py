import heapq
from collections import Counter


def huffman_codes(text):
    """Build prefix-free Huffman codes for characters in text."""
    frequencies = Counter(text)
    if not frequencies:
        return {}
    if len(frequencies) == 1:
        return {next(iter(frequencies)): "0"}

    heap = []
    for sequence, (character, frequency) in enumerate(frequencies.items()):
        heapq.heappush(heap, (frequency, sequence, (character,)))

    sequence = len(heap)
    while len(heap) > 1:
        left_frequency, _, left = heapq.heappop(heap)
        right_frequency, _, right = heapq.heappop(heap)
        heapq.heappush(heap, (left_frequency + right_frequency, sequence, (left, right)))
        sequence += 1

    codes = {}

    def walk(node, prefix):
        if len(node) == 1:
            codes[node[0]] = prefix
            return
        left, right = node
        walk(left, prefix + "0")
        walk(right, prefix + "1")

    walk(heap[0][2], "")
    return codes
