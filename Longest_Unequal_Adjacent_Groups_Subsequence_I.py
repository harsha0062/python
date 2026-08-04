from typing import List

def getLongestSubsequence(words: List[str], groups: List[int]) -> List[str]:
    # Store the selected words
    ans = []

    # Get the number of words
    n = len(words)

    # Traverse through all words
    for i in range(n):
        # Add the first word or a word whose group differs
        # from the group of the previous word
        if i == 0 or groups[i] != groups[i - 1]:
            ans.append(words[i])

    return ans


# Input inside the code
words = ["e", "a", "b", "c", "d"]
groups = [1, 1, 2, 2, 1]

print(getLongestSubsequence(words, groups))