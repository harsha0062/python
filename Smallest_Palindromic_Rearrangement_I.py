from typing import List

def smallestPalindrome(s: str) -> str:
    # Get the length of the string
    n = len(s)

    # If the length is odd, keep the middle character unchanged
    if n % 2 == 1:
        h1 = sorted(s[:n // 2])                  # Sort the left half
        h2 = sorted(s[n // 2 + 1:], reverse=True)  # Sort the right half in reverse order
        return "".join(h1 + [s[n // 2]] + h2)
    else:
        h1 = sorted(s[:n // 2])                  # Sort the left half
        h2 = sorted(s[n // 2:], reverse=True)    # Sort the right half in reverse order
        return "".join(h1 + h2)


# Input inside the code
s = "dcba"

print(smallestPalindrome(s))