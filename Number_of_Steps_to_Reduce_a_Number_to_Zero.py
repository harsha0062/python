def numberOfSteps(num: int) -> int:
    """
    Counts the minimum number of steps to reduce num to 0.
    In each step, if num is even, divide by 2; if odd, subtract 1.
    
    Args:
        num: A non-negative integer
        
    Returns:
        Total number of steps required
    """
    ans = 0  # Initialize step counter
    while num != 0:  # Continue until num becomes 0
        if num % 2 == 0:  # Check if num is even
            num = num // 2  # Divide by 2 (right shift equivalent)
        else:  # num is odd
            num = num - 1  # Subtract 1 to make it even
        ans += 1  # Increment step count after each operation
    return ans  # Return total steps

# Test cases with input inside the code
print("Test Case 1:")
result1 = numberOfSteps(14)
print(f"Input: 14, Output: {result1}")  # Expected: 6

print("\nTest Case 2:")
result2 = numberOfSteps(8)
print(f"Input: 8, Output: {result2}")   # Expected: 4

print("\nTest Case 3:")
result3 = numberOfSteps(0)
print(f"Input: 0, Output: {result3}")   # Expected: 0
