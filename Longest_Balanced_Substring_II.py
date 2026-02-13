def longestBalanced(s: str) -> int:
    """
    Find the length of the longest balanced substring in a string containing 'a', 'b', 'c'.
    A balanced substring has equal counts of each character type within its scope.
    """
    n = len(s)
    res = 0

    # Case 1: Single character runs (all 'a's, all 'b's, or all 'c's)
    # Find longest consecutive run of same character
    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        res = max(res, j - i)
        i = j
    
    # Case 2: Two character balanced substrings (exclude one character type)
    def two(x, y, exclude):
        """
        Find longest balanced substring using only characters x and y (excluding 'exclude').
        Uses prefix sum difference technique: track (count_x - count_y).
        """
        i = 0
        mx = 0
        while i < n:
            if s[i] == exclude:
                i += 1
                continue
            m = {0: i - 1}  # Map difference -> earliest index
            cx, cy = 0, 0   # Counts for x and y
            while i < n and s[i] != exclude:
                if s[i] == x: 
                    cx += 1
                else: 
                    cy += 1
                key = cx - cy  # Balance key
                if key in m: 
                    mx = max(mx, i - m[key])
                else:
                    m[key] = i
                i += 1
        return mx

    # Check all 3 pairs of 2-character combinations
    res = max(res, two('a', 'b', 'c'))
    res = max(res, two('a', 'c', 'b'))
    res = max(res, two('b', 'c', 'a'))

    # Case 3: Three character balanced substring (all 'a','b','c')
    # Track two differences: (count_a - count_b, count_b - count_c)
    m = {(0, 0): -1}
    ca, cb, cc = 0, 0, 0
    for i in range(n):
        if s[i] == 'a': 
            ca += 1
        elif s[i] == 'b':
            cb += 1
        else:
            cc += 1
        key = (ca - cb, cb - cc)
        if key in m:
            res = max(res, i - m[key])
        else: 
            m[key] = i
    
    return res

# Test input
s = "abcabcababcababcc"
print(f"Input: {s}")
print(f"Longest balanced substring length: {longestBalanced(s)}")
