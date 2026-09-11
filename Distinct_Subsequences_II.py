def distinctSubseqII(s: str) -> int:
    # Get the length of the string
    n = len(s)

    # dp[i] stores the number of distinct subsequences
    # that can be formed using the first i characters,
    # including the empty subsequence
    dp = [1] * (n + 1)

    # Store the previous index of each character
    last = {}

    # Modulo value to prevent very large numbers
    mod = 10**9 + 7

    for i in range(n):
        # Every existing subsequence can either include
        # or exclude the current character
        dp[i + 1] = dp[i] * 2

        # If the character appeared before, subtract duplicate subsequences
        if s[i] in last:
            dp[i + 1] -= dp[last[s[i]]]

        # Store the latest index of the current character
        last[s[i]] = i

        # Keep the value manageable
        dp[i + 1] %= mod

    # Exclude the empty subsequence
    return (dp[-1] - 1) % mod


# Input inside the code
s = "abc"

print(distinctSubseqII(s))