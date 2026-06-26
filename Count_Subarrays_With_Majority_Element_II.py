from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        """
        Count subarrays where target appears more than half the length.

        Idea:
        - Convert the array into +1 for target, -1 for non-target.
        - A subarray has target as majority iff its transformed sum > 0.
        - So we need to count pairs of prefix sums (i, j) with prefix[j] > prefix[i].
        """
        n = len(nums)

        # Balance range can go from -n to +n, so shift by n to keep indices non-negative.
        offset = n
        size = 2 * n + 1

        # freq[b] = how many times a prefix balance value b has appeared
        freq = [0] * size

        # Prefix sums count of frequencies up to index b
        # This helps count how many previous balances are smaller than current balance.
        pref = [0] * size

        # Initial prefix balance is 0, which corresponds to index offset
        bal = offset
        freq[bal] = 1
        pref[bal] = 1

        res = 0

        for num in nums:
            # +1 for target, -1 for non-target
            if num == target:
                bal += 1
            else:
                bal -= 1

            # Count previous prefix balances strictly smaller than current balance
            # Those form subarrays with positive sum.
            if bal > 0:
                res += pref[bal - 1]

            # Add current balance to freq and update prefix counts from bal onward
            freq[bal] += 1
            for i in range(bal, size):
                pref[i] += 1

        return res


# Input inside the code
sol = Solution()

nums1 = [1, 2, 2, 2, 1, 2]
target1 = 2
print(sol.countMajoritySubarrays(nums1, target1))

nums2 = [3, 3, 3]
target2 = 3
print(sol.countMajoritySubarrays(nums2, target2))

nums3 = [1, 2, 3, 4]
target3 = 5
print(sol.countMajoritySubarrays(nums3, target3))