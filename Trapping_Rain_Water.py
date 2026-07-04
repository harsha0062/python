from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Return the total amount of trapped rain water.

        Idea:
        - Use two pointers, one from the left and one from the right.
        - Track the highest bar seen so far from both sides:
          leftMax and rightMax.
        - The smaller side determines the water level.
        - Move the pointer with the smaller max inward and add trapped water.
        """
        res = 0
        n = len(height)
        l, r = 0, n - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res


# Test cases inside the code
sol = Solution()

height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height1))  # 6

height2 = [4,2,0,3,2,5]
print(sol.trap(height2))  # 9

height3 = [1,0,2]
print(sol.trap(height3))  # 1