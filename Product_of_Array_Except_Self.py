from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Return an array answer such that answer[i] is the product of all
        elements in nums except nums[i].

        Idea:
        - First pass: store prefix products in ans.
        - Second pass: multiply by postfix products from the right.
        - No division is used.
        - Time: O(n), Space: O(1) extra (output array not counted).
        """
        n = len(nums)
        ans = [1] * n

        # Prefix pass:
        # ans[i] will hold product of all elements to the left of i
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        # Postfix pass:
        # Multiply ans[i] by product of all elements to the right of i
        postfix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans


# Test cases inside the code
sol = Solution()

nums1 = [1, 2, 3, 4]
print(sol.productExceptSelf(nums1))  # [24, 12, 8, 6]

nums2 = [-1, 1, 0, -3, 3]
print(sol.productExceptSelf(nums2))  # [0, 0, 9, 0, 0]

nums3 = [2, 3]
print(sol.productExceptSelf(nums3))  # [3, 2]