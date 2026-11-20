from collections import Counter

VALUES = [12, 7, 19, 3, 25, 11, 8]

def summarize(values: list[int]) -> dict[str, int | float]:
    if not values:
        return {"sum": 0, "maximum": 0, "minimum": 0, "average": 0}
    total = sum(values)
    maximum = max(values)
    minimum = min(values)
    average = total / len(values)
    return {
        "sum": total,
        "maximum": maximum,
        "minimum": minimum,
        "average": average,
    }

def unique(values: list[int]) -> list[int]:
    return list(dict.fromkeys(values))

def frequencies(values: list[int]) -> dict[int, int]:
    return dict(sorted(Counter(values).items()))

def search(values: list[int], target: int) -> int:
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def sorted_copy(values: list[int]) -> list[int]:
    result = values.copy()
    for end in range(len(result) - 1, 0, -1):
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
    return result

def main() -> None:
    print("Utility exercise 35")
    print("Values:", VALUES)
    print("Summary:", summarize(VALUES))
    print("Unique:", unique(VALUES))
    print("Frequencies:", frequencies(VALUES))
    print("Search 19:", search(VALUES, 19))
    print("Sorted:", sorted_copy(VALUES))
    print("Squares:", [value * value for value in VALUES])
    print("Above average:", [value for value in VALUES
          if value > summarize(VALUES)["average"]])

if __name__ == "__main__":
    main()
