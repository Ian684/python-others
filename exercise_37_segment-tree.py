class SegmentTree:
    """Point-update, range-sum segment tree."""
    def __init__(self, values):
        self.size = len(values)
        self.values = [0] * (2 * self.size) if self.size else []
        self.values[self.size:] = values
        for index in range(self.size - 1, 0, -1):
            self.values[index] = self.values[index * 2] + self.values[index * 2 + 1]

    def update(self, index, value):
        if not 0 <= index < self.size:
            raise IndexError("index outside segment tree")
        index += self.size
        self.values[index] = value
        while index > 1:
            index //= 2
            self.values[index] = self.values[index * 2] + self.values[index * 2 + 1]

    def range_sum(self, left, right):
        """Return the inclusive range sum [left, right]."""
        if left < 0 or right < left or right >= self.size:
            raise IndexError("range is outside segment tree")
        left += self.size
        right += self.size + 1
        total = 0
        while left < right:
            if left & 1:
                total += self.values[left]
                left += 1
            if right & 1:
                right -= 1
                total += self.values[right]
            left //= 2
            right //= 2
        return total
