def numDistinct(s: str, t: str) -> int:
    # Get the lengths of both strings
    n = len(s)
    m = len(t)

    # dp[i][j] stores the number of distinct subsequences of s[i:]
    # that match t[j:]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # An empty target string can be formed in exactly one way:
    # by selecting no characters
    for i in range(n + 1):
        dp[i][m] = 1

    # Fill the DP table from bottom to top and right to left
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            # Skip the current character of s
            dp[i][j] = dp[i + 1][j]

            # If the characters match, also use the current characters
            if s[i] == t[j]:
                dp[i][j] += dp[i + 1][j + 1]

    # Return the number of distinct subsequences of s matching t
    return dp[0][0]


# Input inside the code
s = "rabbbit"
t = "rabbit"

print(numDistinct(s, t))