def countSegments(s: str) -> int:
    # Store the total number of segments
    ans = 0

    # Get the length of the string
    n = len(s)

    # Traverse every character in the string
    for i in range(n):
        # A new segment starts when:
        # - The current character is not a space, and
        # - It is either the first character or the previous character is a space
        if s[i] != " " and (i == 0 or s[i - 1] == " "):
            ans += 1

    return ans


# Input inside the code
s = "Hello, my name is Perplexity"

print(countSegments(s))