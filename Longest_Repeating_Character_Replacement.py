class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Return the length of the longest substring that can be turned into
        the same character with at most k replacements.

        Idea:
        - Expand the right pointer.
        - Keep frequency counts of characters in the current window.
        - If the window needs more than k replacements, shrink from the left.
        """
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


# Test cases inside the code
sol = Solution()

print(sol.characterReplacement("ABAB", 2))      # 4
print(sol.characterReplacement("AABABBA", 1))    # 4
print(sol.characterReplacement("AAAA", 2))       # 4
print(sol.characterReplacement("ABCDE", 1))      # 2