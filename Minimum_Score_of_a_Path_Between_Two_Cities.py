def minFlips(s: str) -> int:
    """
    Find minimum flips to make binary string alternating (considering rotations).
    Uses sliding window on doubled string to simulate all rotations efficiently.
    """
    w = len(s)  # Original length
    s *= 2      # Double string to handle rotations: "abc" -> "abcabc"
    n = len(s)

    def solve(tar):
        """
        Calculate min flips for one target pattern (starting with '0' or '1').
        Sliding window tracks mismatches in windows of size w.
        """
        curr = 0                    # Current window mismatches
        prev_tar = [''] * n         # Previous target chars for each position
        tar = tar                   # Current target char
        
        # Initialize first window [0:w)
        for i in range(w):
            if s[i] != tar:         # Count mismatch
                curr += 1
            prev_tar[i] = tar       # Store what we expected here
            tar = '1' if tar == '0' else '0'  # Toggle target
        
        res = curr                   # Best result so far
        
        # Slide window across doubled string
        for i in range(w, n):
            # Remove leaving char: if it was mismatched, decrement
            if s[i-w] != prev_tar[i-w]:
                curr -= 1
            # Add entering char: if mismatched, increment  
            if s[i] != tar:
                curr += 1
            res = min(res, curr)    # Track minimum
            tar = '1' if tar == '0' else '0'  # Toggle for next position
        
        return res

    # Try both possible alternating patterns
    return min(solve('0'), solve('1'))


# Test cases with inputs inside code
print("s='111000' ->", minFlips('111000'))  # Expected: 2
print("s='010' ->", minFlips('010'))        # Expected: 0  
print("s='1110' ->", minFlips('1110'))      # Expected: 1
print("s='100011001' ->", minFlips('100011001'))  # Expected: 3