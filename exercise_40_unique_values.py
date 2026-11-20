"""Utility exercise 40: unique values."""

def unique_values(items: list) -> list:
    return list(dict.fromkeys(items))


if __name__ == "__main__":
    print("Exercise 40: ready")
