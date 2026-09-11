from typing import List
from collections import deque

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    # Store the maximum value for each sliding window
    output = []

    # Store indices of useful elements in decreasing order of values
    q = deque()

    # Left and right boundaries of the sliding window
    l = 0
    r = 0

    while r < len(nums):
        # Remove indices whose values are smaller than the current value
        # because they cannot become the maximum while the current value exists
        while q and nums[q[-1]] < nums[r]:
            q.pop()

        # Add the current index to the deque
        q.append(r)

        # Remove indices that are outside the current window
        if l > q[0]:
            q.popleft()

        # Once the first complete window is formed, record its maximum
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1

        # Expand the window to the right
        r += 1

    return output


# Input inside the code
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(maxSlidingWindow(nums, k))