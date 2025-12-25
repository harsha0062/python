from typing import List

# Function definition (same logic as your code)
def minDeletionSize(strs: List[str]) -> int:
    n = len(strs)          # number of strings
    w = len(strs[0])       # length of each string
    ans = 0                # count of deleted columns
    
    # cur keeps track of built prefixes for each string
    cur = [""] * n

    # iterate column by column
    for j in range(w):
        cur2 = cur[:]      # copy current prefixes

        # add current column character to each prefix
        for i in range(n):
            cur2[i] += strs[i][j]

        # check if prefixes are non-decreasing
        if all(cur2[i] <= cur2[i + 1] for i in range(n - 1)):
            cur = cur2     # accept column
        else:
            ans += 1       # delete column

    return ans


# -------- Input inside the code --------
strs = ["ca", "bb", "ac"]

# Function call
result = minDeletionSize(strs)

# Output
print("Minimum deletions needed:", result)
