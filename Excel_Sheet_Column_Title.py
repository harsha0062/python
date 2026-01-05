# Function to convert a positive integer to its corresponding Excel column title.
# Example: 1 -> "A", 28 -> "AB"
def convertToTitle(c: int) -> str:
    # Start with an empty string that will store the resulting column title.
    s = ""
    # Keep looping until the number becomes 0.
    while c > 0:
        # Decrement by 1 to make the number 0-indexed (Excel columns are 1-indexed).
        c -= 1
        # Find the remainder when divided by 26 and map it to an uppercase letter.
        # 65 is ASCII code for 'A', so 65 + 0 -> 'A', 65 + 25 -> 'Z'.
        b = 65 + (c % 26)
        # Prepend the character to the result string.
        s = chr(b) + s
        # Move to the next "digit" in base-26 representation.
        c = c // 26
    # Return the final Excel column title.
    return s


# Example inputs to test the function.
# You can change these values to test with other numbers.
n1 = 1
n2 = 28
n3 = 701

print(n1, "->", convertToTitle(n1))  # Expected: A
print(n2, "->", convertToTitle(n2))  # Expected: AB
print(n3, "->", convertToTitle(n3))  # Expected: ZY
