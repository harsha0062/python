from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Return the length of the longest consecutive sequence.

        Idea:
        - Put all numbers in a set for O(1) lookups.
        - Only start counting from numbers that are the beginning of a sequence
          (i.e., n-1 is not in the set).
        - Expand forward while the next number exists.
        - Track the maximum sequence length.
        """
        numset = set(nums)
        longest = 0

        for n in numset:
            # Start only from the first number of a sequence
            if (n - 1) not in numset:
                length = 0

                # Count consecutive numbers starting from n
                while (n + length) in numset:
                    length += 1

                longest = max(longest, length)

        return longest


# Test cases inside the code
sol = Solution()

nums1 = [100, 4, 200, 1, 3, 2]
print(sol.longestConsecutive(nums1))  # 4

nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(sol.longestConsecutive(nums2))  # 9

nums3 = []
print(sol.longestConsecutive(nums3))  # 0

nums4 = [1, 2, 0, 1]
print(sol.longestConsecutive(nums4))  # 3