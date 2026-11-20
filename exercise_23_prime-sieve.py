from collections import Counter, deque
import heapq
import math

EXERCISE = 23
TOPIC = "utility-prime-sieve"
VALUES = [12, 7, 19, 3, 25, 11, 8, 19]

def summarize(values):
    if not values:
        return {"sum": 0, "maximum": 0, "minimum": 0, "average": 0}
    total = sum(values)
    return {"sum": total, "maximum": max(values),
            "minimum": min(values), "average": total / len(values)}

def frequencies(values):
    result = Counter(values)
    return dict(sorted(result.items()))

def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def binary_search(values, target):
    left = 0
    right = len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    if left < len(values) and values[left] == target:
        return left
    return -1

def merge_sort(values):
    if len(values) < 2:
        return values
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

def gcd(left, right):
    while right:
        left, right = right, left % right
    return left

def unique_topic_values():
    return sorted(set(VALUES), reverse=True)

def main():
    print("Exercise:", EXERCISE)
    print("Topic:", TOPIC)
    print("Summary:", summarize(VALUES))
    print("Frequency:", frequencies(VALUES))
    print("Linear 19:", linear_search(VALUES, 19))
    print("Binary 19:", binary_search(sorted(VALUES), 19))
    print("Merge sort:", merge_sort(VALUES))
    print("GCD:", gcd(2024, 18))
    print("Unique descending:", unique_topic_values())

if __name__ == "__main__":
    main()

EXERCISE_DETAIL_e9ac3800f8d3_73 = 73
EXERCISE_DETAIL_e9ac3800f8d3_74 = 74
EXERCISE_DETAIL_e9ac3800f8d3_75 = 75
EXERCISE_DETAIL_e9ac3800f8d3_76 = 76
EXERCISE_DETAIL_e9ac3800f8d3_77 = 77
EXERCISE_DETAIL_e9ac3800f8d3_78 = 78
EXERCISE_DETAIL_e9ac3800f8d3_79 = 79
