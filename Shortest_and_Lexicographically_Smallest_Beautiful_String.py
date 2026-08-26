def shortestBeautifulSubstring(s: str, k: int) -> str:
    n = len(s)
    l = 0
    ones = 0
    res = ""

    # Expand the sliding window by moving the right pointer
    for r in range(n):
        if s[r] == "1":
            ones += 1

        # Shrink the window from the left if the number of 1s exceeds k
        while ones > k:
            if s[l] == "1":
                ones -= 1
            l += 1

        # Remove unnecessary leading zeros to keep the substring minimal
        while l < r and s[l] == "0":
            l += 1

        # When the window contains exactly k ones, evaluate the candidate
        if ones == k:
            curr = s[l:r + 1]

            # Update the result if:
            # 1) No result found yet,
            # 2) Current substring is shorter, or
            # 3) Same length but lexicographically smaller
            if (not res or
                len(curr) < len(res) or
                (len(curr) == len(res) and curr < res)):
                res = curr

    return res


# Input inside the code
s = "100011001"
k = 3

print(shortestBeautifulSubstring(s, k))