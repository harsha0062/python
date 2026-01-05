# Function to convert Excel column title (like "A", "AB", "ZY") to its column number
def titleToNumber(c: str) -> int:
    # Initialize sum to 0; this will store the final column number
    sum = 0

    # Traverse each character in the string from left to right
    for i in c:
        # Multiply current sum by 26 (since there are 26 letters, like base-26)
        # Then add the value of current character:
        # 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26
        sum = (sum * 26) + (ord(i) - ord('A') + 1)

    # Return the computed column number
    return sum


# Sample inputs given directly inside the code (no interactive input, no main guard)
example1 = "A"      # Expected 1
example2 = "AB"     # Expected 28
example3 = "ZY"     # Expected 701

# Printing results for the sample inputs
print(example1, "->", titleToNumber(example1))
print(example2, "->", titleToNumber(example2))
print(example3, "->", titleToNumber(example3))
