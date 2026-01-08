from typing import List

# Your original function (unchanged)
def maxDotProduct(nums1: List[int], nums2: List[int]) -> int:
    # Get lengths of both arrays
    n, m = len(nums1), len(nums2)

    # Initialize DP table with negative infinity
    # dp[i][j] will represent the maximum dot product using
    # some non-empty subsequences from nums1[:i] and nums2[:j]
    dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

    # Fill the DP table using the given recurrence
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Current product if we pair nums1[i-1] with nums2[j-1]
            current_prod = nums1[i - 1] * nums2[j - 1]

            # We consider:
            # 1. Taking only this pair (starting a new subsequence)
            # 2. Extending a previous subsequence with this pair
            # 3. Skipping nums1[i-1]
            # 4. Skipping nums2[j-1]
            dp[i][j] = max(
                current_prod,              # start new subsequence with this pair
                current_prod + dp[i - 1][j - 1],  # extend previous subsequence
                dp[i - 1][j],              # skip nums1[i-1]
                dp[i][j - 1]               # skip nums2[j-1]
            )

    # The answer is stored in dp[n][m]
    return dp[n][m]


# Example input inside the code
nums1 = [2, 1, -2, 5]
nums2 = [3, 0, -6]

# Call the function and print the result
result = maxDotProduct(nums1, nums2)
print("Max dot product of two subsequences:", result)
