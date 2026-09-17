def maxPalindromes(s: str, k: int) -> int:
    # Get the length of the string
    n = len(s)

    # ispal[left][right] is True if s[left:right + 1] is a palindrome
    ispal = [[False] * n for _ in range(n)]

    # Check substrings by increasing length
    for length in range(1, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1

            # A substring is a palindrome when:
            # - Its first and last characters are equal
            # - Its inner substring is also a palindrome
            # Lengths 1 and 2 need no inner substring check
            ispal[left][right] = (
                s[left] == s[right]
                and (length <= 2 or ispal[left + 1][right - 1])
            )

    # dp[i] stores the maximum number of non-overlapping palindromes
    # of length at least k using characters from s[0] through s[i]
    dp = [0] * n

    for i in range(n):
        # Option 1: do not use a palindrome ending at index i
        if i > 0:
            dp[i] = dp[i - 1]

        # Check every possible starting index of a palindrome
        # whose length is at least k
        for j in range(i - k + 2):
            if ispal[j][i]:
                # Number of palindromes before index j
                previous = dp[j - 1] if j - 1 >= 0 else 0

                # Select the maximum number of non-overlapping palindromes
                dp[i] = max(dp[i], previous + 1)

    return dp[n - 1]


# Input inside the code
s = "abaccdbbd"
k = 3

print(maxPalindromes(s, k))