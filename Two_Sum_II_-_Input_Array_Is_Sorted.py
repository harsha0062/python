from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two numbers in a sorted array that add up to target.

        Idea:
        - Use two pointers:
          left starts at the beginning
          right starts at the end
        - If the sum is too small, move left forward.
        - If the sum is too large, move right backward.
        - Return 1-based indices as required by the problem.
        """
        i, j = 0, len(numbers) - 1

        while i < j:
            curr = numbers[i] + numbers[j]

            if curr < target:
                i += 1
            elif curr > target:
                j -= 1
            else:
                return [i + 1, j + 1]

        return []


# Test cases inside the code
sol = Solution()

numbers1 = [2, 7, 11, 15]
target1 = 9
print(sol.twoSum(numbers1, target1))  # [1, 2]

numbers2 = [2, 3, 4]
target2 = 6
print(sol.twoSum(numbers2, target2))  # [1, 3]

numbers3 = [-1, 0]
target3 = -1
print(sol.twoSum(numbers3, target3))  # [1, 2]