from typing import List

def isSubsequence(s: str, t: str) -> bool:
    """
    Checks if string s is a subsequence of string t.
    A subsequence means all characters of s appear in t in the same order.
    
    Args:
        s: Potential subsequence string
        t: Main string to check against
        
    Returns:
        True if s is subsequence of t, False otherwise
    """
    m = len(s)  # Length of subsequence string
    n = len(t)  # Length of main string
    i, j = 0, 0  # Pointers for s and t respectively
    
    # Traverse both strings with two pointers
    while i < m and j < n:
        # If characters match, move to next character in s
        if s[i] == t[j]:
            i += 1
        # Always move to next character in t
        j += 1
    
    # If we've matched all characters of s (i reaches end of s)
    return i >= m

# Test cases with input inside the code
print("Test Case 1:")
result1 = isSubsequence("abc", "ahbgdc")
print(f"Input: s='abc', t='ahbgdc'")
print(f"Output: {result1}")  # Expected: True

print("\nTest Case 2:")
result2 = isSubsequence("axc", "ahbgdc")
print(f"Input: s='axc', t='ahbgdc'")
print(f"Output: {result2}")  # Expected: False

print("\nTest Case 3:")
result3 = isSubsequence("", "ahbgdc")
print(f"Input: s='', t='ahbgdc'")
print(f"Output: {result3}")   # Expected: True

print("\nTest Case 4:")
result4 = isSubsequence("abc", "abc")
print(f"Input: s='abc', t='abc'")
print(f"Output: {result4}")   # Expected: True
