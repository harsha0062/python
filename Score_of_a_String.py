def scoreOfString(s):
    """
    Calculates the score of a string by summing absolute differences
    between ASCII values of adjacent characters.
    
    Args:
        s (str): Input string
    
    Returns:
        int: Total score
    """
    ans = 0  # Initialize score accumulator
    for i in range(1, len(s)):  # Loop from second char to end
        f = ord(s[i-1])         # ASCII value of previous char
        c = ord(s[i])           # ASCII value of current char
        ans += abs(f - c)       # Add absolute difference to total
    return ans                  # Return final score

# Test cases with inputs directly in code
print(scoreOfString("hello"))     # Example: "hello" -> |104-101| + |101-108| + |108-108| + |108-111| = 11
print(scoreOfString("zaz"))      # Example: "zaz" -> |122-97| + |97-122| = 50
