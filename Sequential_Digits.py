from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # String containing digits in increasing order
        c = '123456789'
        res = []

        # Try every possible starting index
        for i in range(9):
            # Try every possible ending index from i to the end
            for j in range(i, 9):
                curr = c[i:j+1]
                num = int(curr)
                if low <= num <= high:
                    res.append(num)

        # Return results in sorted order
        res.sort()
        return res


# Input inside the code
low = 100
high = 3000

sol = Solution()
print(sol.sequentialDigits(low, high))