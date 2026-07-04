from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Return the maximum water that can be contained.

        Idea:
        - Use two pointers:
          i starts at the left end
          j starts at the right end
        - The area is determined by:
          width * min(height[i], height[j])
        - Move the pointer with the smaller height inward, because that is the
          only way to possibly find a bigger area.
        """
        n = len(height)
        i = 0
        j = n - 1
        res = 0

        while i < j:
            area = (j - i) * min(height[i], height[j])
            res = max(res, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return res


# Test cases inside the code
sol = Solution()

height1 = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height1))  # 49

height2 = [1,1]
print(sol.maxArea(height2))  # 1

height3 = [4,3,2,1,4]
print(sol.maxArea(height3))  # 16

height4 = [1,2,1]
print(sol.maxArea(height4))  # 2