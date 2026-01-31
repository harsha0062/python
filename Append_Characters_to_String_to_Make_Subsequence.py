def appendCharacters(s: str, t: str) -> int:
    """
    Returns minimum number of characters to append to s to make t a subsequence.
    Uses two-pointer technique to find longest common subsequence prefix.
    
    Args:
        s: Source string
        t: Target subsequence string
        
    Returns:
        Number of characters needed to append to make t a subsequence of s
    """
    ans = 0  # Not used in final calculation, kept for consistency
    m, n = len(s), len(t)  # Lengths of s and t
    i, j = 0, 0  # Pointers for s and t
    
    # Two-pointer traversal
    while i < m and j < n:
        # If characters match, advance both pointers
        if s[i] == t[j]:
            j += 1  # Progress in target string
        i += 1  # Always advance in source string
    
    # Remaining characters in t need to be appended
    return len(t) - j

# Test cases with input inside the code
print("Test Case 1:")
result1 = appendCharacters("coaching", "codiing")
print(f"Input: s='coaching', t='codiing'")
print(f"Output: {result1}")  # Expected: 2 ("ng" needs to be appended)

print("\nTest Case 2:")
result2 = appendCharacters("abcde", "a")
print(f"Input: s='abcde', t='a'")
print(f"Output: {result2}")  # Expected: 0 (already subsequence)

print("\nTest Case 3:")
result3 = appendCharacters("z", "abcde")
print(f"Input: s='z', t='abcde'")
print(f"Output: {result3}")  # Expected: 5 (append all "abcde")

print("\nTest Case 4:")
result4 = appendCharacters("", "z")
print(f"Input: s='', t='z'")
print(f"Output: {result4}")  # Expected: 1
