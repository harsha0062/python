from typing import List
from collections import defaultdict

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """
        Find the maximum length of a subsequence that follows the square-chain pattern.

        Pattern idea:
        - Start from some number x.
        - If x exists at least twice, you can use it as a repeated pair in the chain.
        - Then move to x^2, then (x^2)^2, and so on while the values exist.
        - Special case for 1:
          since 1^2 = 1, the best you can do is use an odd count of 1s.
        """
        fm = defaultdict(int)

        # Count frequency of each number
        for i in nums:
            fm[i] += 1

        # Handle 1 separately:
        # We can take all 1s if count is odd, otherwise count-1
        ones = fm[1]
        res = ones if ones % 2 == 1 else max(0, ones - 1)

        # Try starting the chain from every number except 1
        for num in fm:
            if num == 1:
                continue

            total = 0
            curr = num

            # As long as current number exists with frequency at least 2,
            # we can take it in pairs and continue the square chain.
            while curr in fm and fm[curr] >= 2:
                total += 2
                curr *= curr

            # If the final squared value exists, we can add one more
            # to complete the chain.
            if curr in fm:
                total += 1
            else:
                # If the chain breaks, remove the last incomplete step effect
                total -= 1

            res = max(res, total)

        return res


# Input inside the code
sol = Solution()

nums1 = [1, 1, 1, 1, 2, 2, 4, 4, 16]
print(sol.maximumLength(nums1))

nums2 = [3, 3, 9, 9, 81]
print(sol.maximumLength(nums2))

nums3 = [1, 1, 1, 2, 2, 4]
print(sol.maximumLength(nums3))