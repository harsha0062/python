from typing import List
from collections import defaultdict

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Map each value to its rank
        hmap = defaultdict(int)

        # Copy and sort the array
        sortarr = arr.copy()
        sortarr.sort()

        rank = 1

        # Assign ranks to sorted values
        for i in range(len(arr)):
            if i > 0 and sortarr[i - 1] < sortarr[i]:
                rank += 1
            hmap[sortarr[i]] = rank

        # Replace each element with its rank
        for i in range(len(arr)):
            arr[i] = hmap[arr[i]]

        return arr


# Input inside the code
arr = [40, 10, 20, 30, 20]

sol = Solution()
print(sol.arrayRankTransform(arr))