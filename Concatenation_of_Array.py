def getConcatenation(nums):
    """
    Returns array concatenated with itself (nums + nums).
    Time: O(n), Space: O(n)
    """
    return nums * 2  # Python list multiplication creates two copies

# Test inputs directly in code
print(getConcatenation([1, 2, 1]))     # Output: [1, 2, 1, 1, 2, 1]
print(getConcatenation([1, 3, 2, 1]))  # Output: [1, 3, 2, 1, 1, 3, 2, 1]
print(getConcatenation([]))            # Output: []
print(getConcatenation([5]))           # Output: [5, 5]
