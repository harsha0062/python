def containsDuplicate(nums):
    """
    Returns True if any value appears at least twice in the array,
    False if every element is distinct.
    Time: O(n), Space: O(n)
    """
    l = set(nums)           # Convert to set (removes duplicates automatically)
    return len(l) != len(nums)  # Different lengths = duplicates exist

# Test cases with inputs directly in code
print(containsDuplicate([1, 2, 3, 1]))      # True (1 appears twice)
print(containsDuplicate([1, 2, 3, 4]))      # False (all unique)
print(containsDuplicate([1]))               # False (single element)
print(containsDuplicate([]))                # False (empty array)
print(containsDuplicate([1, 1]))            # True (both same)
