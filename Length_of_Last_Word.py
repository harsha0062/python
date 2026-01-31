def lengthOfLastWord(s: str) -> int:
    """
    Returns the length of the last word in the string.
    A word is a maximal substring consisting of non-space characters.
    Automatically handles multiple trailing spaces.
    
    Args:
        s: String containing words separated by spaces
        
    Returns:
        Length of the last word
    """
    words = [word for word in s.split(" ") if word]  # Split and filter empty strings
    return len(words[-1]) if words else 0            # Return last word length or 0

# Test cases with input inside the code
print("Test Case 1:")
result1 = lengthOfLastWord("Hello World")
print(f"Input:  'Hello World'")
print(f"Output: {result1}")  # Expected: 5

print("\nTest Case 2:")
result2 = lengthOfLastWord("   fly me   to   the moon  ")
print(f"Input:  '   fly me   to   the moon  '")
print(f"Output: {result2}")  # Expected: 4

print("\nTest Case 3:")
result3 = lengthOfLastWord("luffy is still joyboy")
print(f"Input:  'luffy is still joyboy'")
print(f"Output: {result3}")  # Expected: 6

print("\nTest Case 4:")
result4 = lengthOfLastWord("   ")
print(f"Input:  '   '")
print(f"Output: {result4}")  # Expected: 0
