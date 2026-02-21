def reverseBits(n: int) -> int:
    """
    Reverses the bits of a 32-bit unsigned integer n.
    
    Args:
        n: 32-bit unsigned integer whose bits need to be reversed
        
    Returns:
        The integer with reversed bits (still as a 32-bit number)
    """
    binary = format(n, '032b')  # Convert to 32-bit binary string (pad with leading zeros)
    st = binary[::-1]           # Reverse the binary string using slicing
    return int(st, 2)           # Convert reversed binary back to integer

# Input: Test the function with sample inputs
n1 = 43261596   # Binary: 00000010100101000001111010011100
result1 = reverseBits(n1)
print(f"Input: {n1}")
print(f"Binary: {format(n1, '032b')}")
print(f"Reversed: {format(result1, '032b')}")
print(f"Output: {result1}\n")  # Expected: 964176192 (Binary: 00111001011110000010100101000000)

n2 = 4294967293  # Binary: 11111111111111111111111111111101
result2 = reverseBits(n2)
print(f"Input: {n2}")
print(f"Binary: {format(n2, '032b')}")
print(f"Reversed: {format(result2, '032b')}")
print(f"Output: {result2}")  # Expected: 3221225471 (Binary: 10111111111111111111111111111111)
