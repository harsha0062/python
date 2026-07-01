from typing import List
from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Count the number of substrings containing at least one 'a', one 'b', and one 'c'.

        Idea:
        - Use a sliding window [l...r].
        - Expand r and count characters in the current window.
        - Once the window contains all 'a', 'b', and 'c',
          every substring starting at l and ending at r, r+1, ..., n-1 is valid.
          So we add (n - r) to the answer.
        - Then move l forward to look for more valid substrings.
        """
        n = len(s)
        fm = defaultdict(int)
        res = 0
        l = 0

        for r in range(n):
            # Include current character in the window
            fm[s[r]] += 1

            # While the current window contains at least one of each 'a', 'b', and 'c'
            while l <= r and all(fm[c] > 0 for c in ['a', 'b', 'c']):
                # Every substring that starts at l and ends at r or beyond is valid
                res += n - r

                # Shrink the window from the left
                fm[s[l]] -= 1
                l += 1

        return res


# Input inside the code
sol = Solution()

s1 = "abcabc"
print(sol.numberOfSubstrings(s1))

s2 = "aaacb"
print(sol.numberOfSubstrings(s2))

s3 = "abc"
print(sol.numberOfSubstrings(s3))