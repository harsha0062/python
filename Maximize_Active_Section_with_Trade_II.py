from bisect import bisect_left, bisect_right
from typing import List

class SegmentTree:
    def __init__(self, values: List[int]):
        # Number of elements in the array
        self.n = len(values)
        # Segment tree array, sized safely as 4 * n
        self.tree = [0] * (4 * self.n)

        # Build only if there are values
        if self.n > 0:
            self._build(1, 0, self.n - 1, values)

    def _build(self, node: int, left: int, right: int, values: List[int]) -> None:
        # Leaf node
        if left == right:
            self.tree[node] = values[left]
            return

        mid = (left + right) // 2
        self._build(node * 2, left, mid, values)
        self._build(node * 2 + 1, mid + 1, right, values)

        # Store maximum of children
        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, query_left: int, query_right: int) -> int:
        # Invalid range
        if query_left > query_right:
            return 0

        return self._query(1, 0, self.n - 1, query_left, query_right)

    def _query(self, node: int, left: int, right: int, query_left: int, query_right: int) -> int:
        # Current segment fully inside query range
        if query_left <= left and right <= query_right:
            return self.tree[node]

        mid = (left + right) // 2
        answer = 0

        # Query left child if needed
        if query_left <= mid:
            answer = max(answer, self._query(node * 2, left, mid, query_left, query_right))

        # Query right child if needed
        if query_right > mid:
            answer = max(answer, self._query(node * 2 + 1, mid + 1, right, query_left, query_right))

        return answer


def maxActiveSectionsAfterTrade(s: str, queries: List[List[int]]) -> List[int]:
    """
    For each query [left, right], compute the maximum possible active sections
    after trading sections inside the range.
    """
    n = len(s)
    original_ones = s.count("1")

    zero_lengths = []
    zero_starts = []
    zero_ends = []

    # Identify all consecutive zero blocks
    index = 0
    while index < n:
        start = index
        while index < n and s[index] == s[start]:
            index += 1

        # Store zero blocks only
        if s[start] == "0":
            zero_lengths.append(index - start)
            zero_starts.append(start)
            zero_ends.append(index - 1)

    zero_count = len(zero_lengths)

    # If fewer than 2 zero blocks, no useful trade can happen
    if zero_count < 2:
        return [original_ones for _ in queries]

    # Gains from merging adjacent zero blocks
    gains = [zero_lengths[i] + zero_lengths[i + 1] for i in range(zero_count - 1)]
    segment_tree = SegmentTree(gains)

    answers = []

    for left, right in queries:
        # Find the first zero block that intersects or comes after left
        first_block = bisect_left(zero_ends, left)
        # Find the last zero block that starts before or at right
        last_block = bisect_right(zero_starts, right) - 1

        # If query range does not cover at least two zero blocks, no improvement
        if first_block >= zero_count or last_block < 0 or first_block >= last_block:
            answers.append(original_ones)
            continue

        # Length of the part of the first block inside the query
        first_length = zero_ends[first_block] - max(zero_starts[first_block], left) + 1
        # Length of the part of the last block inside the query
        last_length = min(zero_ends[last_block], right) - zero_starts[last_block] + 1

        # If the query touches exactly two zero blocks, compute directly
        if first_block + 1 == last_block:
            best_gain = first_length + last_length
            answers.append(original_ones + best_gain)
            continue

        # Gain from merging first block with next one
        left_boundary_gain = first_length + zero_lengths[first_block + 1]
        # Gain from merging previous block with last block
        right_boundary_gain = zero_lengths[last_block - 1] + last_length
        # Best gain from any internal adjacent pair fully inside the query
        internal_gain = segment_tree.query(first_block + 1, last_block - 2)

        best_gain = max(left_boundary_gain, right_boundary_gain, internal_gain)
        answers.append(original_ones + best_gain)

    return answers


# Input inside the code
s = "1100011000"
queries = [[0, 5], [2, 8], [1, 9]]

print(maxActiveSectionsAfterTrade(s, queries))