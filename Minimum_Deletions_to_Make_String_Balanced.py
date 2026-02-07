def minimumDeletions(s: str) -> int:
    """
    Returns the minimum number of deletions needed to make the string 
    have all 'a's followed by all 'b's (or all 'b's followed by all 'a's).
    
    Approach:
    - Track remaining 'a's as we traverse left to right
    - Track 'b's seen so far
    - At each position, cost = remaining 'a's + 'b's seen so far
    - Return minimum cost found
    """
    n = len(s)
    a_count = sum(1 for c in s if c == "a")  # Total 'a's in string
    
    b_count = 0  # 'b's encountered so far
    min_deletions = n  # Initialize with maximum possible deletions
    
    for ch in s:
        if ch == "a":
            a_count -= 1  # One less 'a' remaining
        min_deletions = min(min_deletions, a_count + b_count)  # Update min cost
        if ch == "b":
            b_count += 1  # One more 'b' seen
    
    return min_deletions

# Test inputs
test_cases = [
    "aab",      # Expected: 0 (already valid)
    "aaabbb",   # Expected: 0 (already valid)  
    "aaa",      # Expected: 0 (all 'a's valid)
    "bbb",      # Expected: 0 (all 'b's valid)
    "abab",     # Expected: 2
    "aabaabb",  # Expected: 2
]

# Run tests
for i, test_str in enumerate(test_cases, 1):
    result = minimumDeletions(test_str)
    print(f"Test {i}: s='{test_str}' -> {result}")
