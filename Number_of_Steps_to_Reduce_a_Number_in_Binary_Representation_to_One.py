def numSteps(s: str) -> int:
    """
    Simulate the process of reducing a binary number to 1 by:
    - If even (ends with 0): divide by 2 (remove last digit)
    - If odd (ends with 1): add 1 (flip all trailing 1s to 0s and first 0 to 1)
    
    Args:
        s: Binary string representation of the number
    
    Returns:
        Total number of steps required to reduce to 1
    """
    n = len(s)
    carry = 0      # Tracks if we need to carry over 1 (when we hit odd number)
    res = 0        # Total steps counter
    
    # Process from right to left (LSB to MSB)
    for i in range(n-1, 0, -1):  # Stop at index 1 (leave MSB for final handling)
        curr = int(s[i]) + carry  # Current bit + any carry from previous
        
        if curr == 1:  # Odd case: add 1 (costs 2 steps: +1 then /2)
            res += 2
            carry = 1  # Set carry for next bit (like flipping trailing 1s)
        else:          # Even case: just divide by 2 (costs 1 step)
            res += 1
            carry = 0  # No carry needed
    
    # Handle the final MSB + any remaining carry
    return res + carry

# Test input - hardcoded as requested
s = "1101"  # Example: 13 in binary (should take 6 steps: 1101 -> 1110 -> 111 -> 1000 -> 100 -> 10 -> 1)

# Print result
print(f"Input: {s}")
print(f"Steps required: {numSteps(s)}")
