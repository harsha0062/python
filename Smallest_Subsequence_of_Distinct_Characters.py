def smallestSubsequence(s: str) -> str:
    """
    Return the lexicographically smallest subsequence of s
    that contains all distinct characters exactly once.
    """
    n = len(s)

    # Store the last position of every character
    last = {}
    for i, c in enumerate(s):
        last[c] = i

    # Stack-like list to build the answer
    res = []

    for i, c in enumerate(s):
        # If character is already in result, skip it
        if c in res:
            continue

        # Remove bigger characters from the end if they appear later again
        while res and c < res[-1] and i < last[res[-1]]:
            res.pop()

        # Add current character
        res.append(c)

    return "".join(res)


# Input inside the code
s = "cbacdcbc"

print(smallestSubsequence(s))