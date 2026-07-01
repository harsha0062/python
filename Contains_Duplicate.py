from typing import List

# Method 1: Using set conversion
def containsDuplicate_method1(nums):
    """
    Returns True if any value appears at least twice.
    Idea:
    - A set removes duplicates automatically.
    - If the set is smaller than the original list, duplicates existed.
    """
    return len(set(nums)) != len(nums)


# Method 2: Using a visited set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Returns True if any value appears at least twice.
        Idea:
        - Keep a set of numbers we have already seen.
        - If the current number is already in the set, it is a duplicate.
        """
        visit = set()

        for i in nums:
            if i not in visit:
                visit.add(i)
            else:
                return True

        return False


# Test cases inside the code
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1]
nums4 = []
nums5 = [1, 1]

print(containsDuplicate_method1(nums1))  # True
print(containsDuplicate_method1(nums2))  # False
print(containsDuplicate_method1(nums3))  # False
print(containsDuplicate_method1(nums4))  # False
print(containsDuplicate_method1(nums5))  # True

sol = Solution()
print(sol.containsDuplicate(nums1))  # True
print(sol.containsDuplicate(nums2))  # False
print(sol.containsDuplicate(nums3))  # False
print(sol.containsDuplicate(nums4))  # False
print(sol.containsDuplicate(nums5))  # True