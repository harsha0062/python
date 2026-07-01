from collections import defaultdict, Counter

# Method 1: Using defaultdict
def isAnagram_method1(s: str, t: str) -> bool:
    """
    Returns True if t is an anagram of s, otherwise False.

    Method 1:
    - Count frequency of each character in both strings using defaultdict.
    - If lengths are different, they cannot be anagrams.
    - Compare the frequency maps.
    """
    counts = defaultdict(int)
    countt = defaultdict(int)

    # If lengths are different, not an anagram
    if len(s) != len(t):
        return False

    # Count characters in both strings
    for i in range(len(s)):
        counts[s[i]] += 1
        countt[t[i]] += 1

    # Compare character frequencies
    for ch in counts:
        if counts[ch] != countt.get(ch, 0):
            return False

    return True


# Method 2: Using Counter
def isAnagram_method2(s: str, t: str) -> bool:
    """
    Returns True if t is an anagram of s, otherwise False.

    Method 2:
    - Counter automatically counts frequencies of characters.
    - Two strings are anagrams if their Counters are equal.
    """
    return Counter(s) == Counter(t)


# Test cases with inputs directly in code
print("Method 1 Results:")
print(isAnagram_method1("anagram", "nagaram"))   # True
print(isAnagram_method1("rat", "car"))           # False
print(isAnagram_method1("a", "a"))               # True
print(isAnagram_method1("", ""))                 # True
print(isAnagram_method1("ab", "ba"))             # True
print(isAnagram_method1("hello", "billion"))     # False

print("\nMethod 2 Results:")
print(isAnagram_method2("anagram", "nagaram"))   # True
print(isAnagram_method2("rat", "car"))           # False
print(isAnagram_method2("a", "a"))               # True
print(isAnagram_method2("", ""))                 # True
print(isAnagram_method2("ab", "ba"))             # True
print(isAnagram_method2("hello", "billion"))     # False