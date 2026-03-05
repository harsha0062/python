def minOperations(s: str) -> int:
    """
    Calculates the minimum number of operations to make the string alternating.
    An alternating string follows the pattern '010101...' or '101010...'.
    
    Args:
        s: Binary string consisting of '0's and '1's
    
    Returns:
        Minimum operations needed to make string alternating
    """
    start0 = 0  # Count of changes needed for pattern starting with '0' (010101...)
    
    # Iterate through each character in the string
    for i in range(len(s)):
        if i % 2 == 0:  # Even indices (0,2,4...) should be '0' in start0 pattern
            if s[i] == '0':
                continue  # Already correct, no change needed
            else:
                start0 += 1  # Need to change '1' to '0'
        else:  # Odd indices (1,3,5...) should be '1' in start0 pattern
            if s[i] == '1':
                continue  # Already correct, no change needed
            else:
                start0 += 1  # Need to change '0' to '1'
    
    # start0 = operations for pattern "010101..."
    # len(s) - start0 = operations for opposite pattern "101010..."
    # Return minimum of both possibilities
    return min(start0, len(s) - start0)

# Test cases with input directly in code
test_cases = [
    "0100",    # Expected: 1 (change to "0101" or "1010")
    "10",      # Expected: 0 (already alternating)
    "1111",    # Expected: 2 (change to "1010")
    "00",      # Expected: 1 (change to "01" or "10")
    "010101"   # Expected: 0 (already perfect)
]

# Run all test cases
print("Testing minOperations function:")
print("=" * 40)
for i, test_str in enumerate(test_cases, 1):
    result = minOperations(test_str)
    print(f"Test {i}: s='{test_str}' -> {result} operations")

print("\nDetailed example walkthrough:")
print("s = '0100'")
print("- Pattern '0101': positions 0:'0'(✓), 1:'1'(✓), 2:'0'(✓), 3:'0'(✗→1) = 1 op")
print("- Pattern '1010': positions 0:'0'(✗→1), 1:'1'(✓), 2:'0'(✗→1), 3:'0'(✓) = 2 op")
print("Minimum = 1")
