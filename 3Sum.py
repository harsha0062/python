from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Return all unique triplets [a, b, c] such that a + b + c == 0.

        Idea:
        - Sort the array.
        - Fix one number nums[i].
        - Use two pointers j and k to find pairs that sum to -nums[i].
        - Skip duplicates to avoid repeated triplets.
        """
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            # Skip duplicate fixed values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since array is sorted, if nums[i] > 0, no triplet can sum to 0
            if nums[i] > 0:
                break

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicate values for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate values for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans


# Test cases inside the code
sol = Solution()

nums1 = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums1))  # [[-1, -1, 2], [-1, 0, 1]]

nums2 = [0, 1, 1]
print(sol.threeSum(nums2))  # []

nums3 = [0, 0, 0]
print(sol.threeSum(nums3))  # [[0, 0, 0]]