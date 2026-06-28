from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        """
        Return the maximum possible value of the last element after:
        1. Rearranging the array in any order.
        2. Decrementing elements any number of times.
        3. Making sure:
           - arr[0] == 1
           - arr[i] - arr[i-1] <= 1 for all i

        Greedy idea:
        - Sort the array.
        - Start with ans = 1.
        - For each next number:
          if it is at least ans + 1, we can increase ans by 1.
          Otherwise, leave ans unchanged.
        """
        arr.sort()

        # The smallest valid value must be 1
        ans = 1

        # Try to extend the sequence as much as possible
        for i in range(1, len(arr)):
            if arr[i] >= ans + 1:
                ans += 1

        return ans


# Input inside the code
sol = Solution()

arr1 = [2, 2, 1, 2, 1]
print(sol.maximumElementAfterDecrementingAndRearranging(arr1))

arr2 = [100, 1, 1000]
print(sol.maximumElementAfterDecrementingAndRearranging(arr2))

arr3 = [1, 2, 3, 4, 5]
print(sol.maximumElementAfterDecrementingAndRearranging(arr3))