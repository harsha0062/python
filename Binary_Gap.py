def binaryGap(n: int) -> int:
    """
    Finds the binary gap in a positive integer n.
    Binary gap is the number of consecutive zeros between two consecutive ones in binary representation.
    Returns the length of the longest binary gap.
    """
    curr = 0      # Current bit position counter
    prev = -1     # Position of previous '1' bit (-1 means no previous '1' found)
    result = 0    # Maximum gap found so far

    while n > 0:
        if (n & 1) > 0:  # Check if current bit is 1 (LSB)
            # Update result only if we have found a previous '1'
            result = max(result, curr - prev) if prev != -1 else result
            prev = curr    # Update previous '1' position
        curr += 1          # Move to next bit position
        n >>= 1            # Right shift to process next bit

    return result

# Test cases with input inside the code
print("Testing binaryGap function:")
print(f"Input: 22 (binary: 10110)")
print(f"Output: {binaryGap(22)}")  # Expected: 2 (gap between 2nd and 3rd 1)

print(f"\nInput: 5 (binary: 101)")
print(f"Output: {binaryGap(5)}")   # Expected: 2

print(f"\nInput: 8 (binary: 1000)")
print(f"Output: {binaryGap(8)}")   # Expected: 0 (no gap)

print(f"\nInput: 15 (binary: 1111)")
print(f"Output: {binaryGap(15)}")  # Expected: 0 (no zeros between 1s)

print(f"\nInput: 1041 (binary: 10000010001)")
print(f"Output: {binaryGap(1041)}") # Expected: 5
