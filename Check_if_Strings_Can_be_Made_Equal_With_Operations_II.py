from collections import Counter

def checkStrings(s1: str, s2: str) -> bool:
    """
    Check if s1 can be transformed into s2 by swapping characters within even/odd positions only.
    Even positions (0,2,4,...): s1[::2] must have same character frequencies as s2[::2]
    Odd positions  (1,3,5,...): s1[1::2] must have same character frequencies as s2[1::2]
    """
    # Compare frequency counters for even positions (indices 0,2,4,...)
    even_s1 = Counter(s1[::2])
    even_s2 = Counter(s2[::2])
    
    # Compare frequency counters for odd positions (indices 1,3,5,...)
    odd_s1 = Counter(s1[1::2])
    odd_s2 = Counter(s2[1::2])
    
    # Both even and odd position character counts must match exactly
    return even_s1 == even_s2 and odd_s1 == odd_s2


# Test cases with inputs inside code
print("s1='aaab', s2='baaa' ->", checkStrings('aaab', 'baaa'))
# even: aa==ba ✓, odd: ab==aa ✗ → False

print("s1='abbb', s2='bbab' ->", checkStrings('abbb', 'bbab'))
# even: ab==bb ✗ → False

print("s1='bacd', s2='dbac' ->", checkStrings('bacd', 'dbac'))
# even: bc==dc ✗ → False

print("s1='aabbccdd', s2='bbccddaa' ->", checkStrings('aabbccdd', 'bbccddaa'))
# even: a,c == b,d ✗ → False

# Visualize counters:
print("\nCounter breakdown for s1='aaab', s2='baaa':")
s1, s2 = 'aaab', 'baaa'
print(f"Even positions s1[::2]='{s1[::2]}' → {Counter(s1[::2])}")
print(f"Even positions s2[::2]='{s2[::2]}' → {Counter(s2[::2])}")
print(f"Odd  positions s1[1::2]='{s1[1::2]}' → {Counter(s1[1::2])}")
print(f"Odd  positions s2[1::2]='{s2[1::2]}' → {Counter(s2[1::2])}")