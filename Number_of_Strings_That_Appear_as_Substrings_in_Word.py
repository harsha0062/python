from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """
        Count how many strings in `patterns` appear as substrings in `word`.

        Idea:
        - Check each pattern one by one.
        - If pattern is found inside `word`, increase the answer.

        Time complexity: O(len(patterns) * len(word)) in the worst case.
        Space complexity: O(1)
        """
        count = 0

        # Check each pattern
        for p in patterns:
            if p in word:
                count += 1

        return count


# Input inside the code
sol = Solution()

patterns1 = ["a", "abc", "bc", "d"]
word1 = "abc"
print(sol.numOfStrings(patterns1, word1))

patterns2 = ["a", "b", "c"]
word2 = "aaaaab"
print(sol.numOfStrings(patterns2, word2))

patterns3 = ["leetcode", "et", "code"]
word3 = "leetcode"
print(sol.numOfStrings(patterns3, word3))