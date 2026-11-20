"""Utility exercise 34: word count."""

def word_count(text: str) -> dict[str, int]:
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    print("Exercise 34: ready")
