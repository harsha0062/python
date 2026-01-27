from collections import Counter

def isAnagram(s, t):
    """
    Returns True if t is an anagram of s (same characters, same frequencies),
    False otherwise. Time: O(n), Space: O(n)
    """
    return Counter(s) == Counter(t)  # Counter equality checks char frequencies

# Test cases with inputs directly in code
print(isAnagram("anagram", "nagaram"))     # True
print(isAnagram("rat", "car"))             # False
print(isAnagram("a", "a"))                 # True
print(isAnagram("", ""))                   # True
print(isAnagram("ab", "ba"))               # True
print(isAnagram("hello", "billion"))       # False