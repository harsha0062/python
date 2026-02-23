def hasAllCodes(s: str, k: int) -> bool:
    need = 1 << k  # Total number of possible binary codes of length k (2^k)
    got = set()    # Set to store unique substrings of length k found in s

    # Slide window of size k over the string s
    for i in range(len(s) - k + 1):
        temp = s[i:i + k]  # Extract substring of length k starting at i
        got.add(temp)      # Add to set (duplicates auto-handled)
        if len(got) == need:  # Early return if all codes found
            return True
    
    # Check if we found all required codes
    return len(got) == need

# Test inputs
s = "00110110"  # Input string
k = 2           # Code length

# Call the function and print result
result = hasAllCodes(s, k)
print(f"Input: s='{s}', k={k}")
print(f"Output: {result}")  # Expected: True (contains 00, 01, 10, 11)

# Additional test case
s2 = "0110"
k2 = 1
result2 = hasAllCodes(s2, k2)
print(f"\nInput: s='{s2}', k={k2}")
print(f"Output: {result2}")  # Expected: True (contains 0, 1)

# Another test case
s3 = "0110"
k3 = 2
result3 = hasAllCodes(s3, k3)
print(f"\nInput: s='{s3}', k={k3}")
print(f"Output: {result3}")  # Expected: False (missing 11)
