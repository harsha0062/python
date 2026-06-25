from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # This is the same brute-force idea as your code:
        # try every subarray and count how many times `target` appears.
        n = len(nums)
        res = 0

        for i in range(n):
            targetc = 0
            for j in range(i, n):
                if nums[j] == target:
                    targetc += 1

                # target is a majority if its count is strictly greater than half
                if targetc > ((j - i + 1) // 2):
                    res += 1

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