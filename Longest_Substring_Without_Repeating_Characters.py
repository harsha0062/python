class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Return the length of the longest substring without repeating characters.

        Idea:
        - Use a sliding window [l..r].
        - Keep a set of characters currently in the window.
        - If s[r] repeats, shrink from the left until it is removed.
        - Update the maximum window length.
        """
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res


# Test cases inside the code
sol = Solution()

print(sol.lengthOfLongestSubstring("abcabcbb"))  # 3
print(sol.lengthOfLongestSubstring("bbbbb"))     # 1
print(sol.lengthOfLongestSubstring("pwwkew"))    # 3
print(sol.lengthOfLongestSubstring(""))          # 0
print(sol.lengthOfLongestSubstring(" "))          # 1