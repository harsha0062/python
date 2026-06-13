from typing import List

def mapWordWeights(words: List[str], weights: List[int]) -> str:
    """
    Map each word to a character based on its total weight.

    For each word:
        1. For each character c in the word:
            - Compute index i = ord(c) - ord('a')  (0 for 'a', 1 for 'b', ..., 25 for 'z')
            - Add weights[i] to the current sum.
        2. Compute w = curr % 26.
        3. Compute rev = 25 - w.
        4. Map rev back to a character: chr(rev + ord('a')).
        5. Append this character to the result string.

    Return the concatenated result string.
    """
    res = ''

    for w in words:
        curr = 0
        for c in w:
            i = ord(c) - ord('a')
            curr += weights[i]

        w_val = curr % 26
        rev = 25 - w_val
        res += chr(rev + ord('a'))

    return res


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
words1 = ["abc", "z"]
weights1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0]

print("words1 =", words1)
print("weights1 =", weights1)
print("mapWordWeights =", mapWordWeights(words1, weights1))

# Trace for "abc":
# a -> index 0 -> weight 1
# b -> index 1 -> weight 2
# c -> index 2 -> weight 3
# curr = 1 + 2 + 3 = 6
# w = 6 % 26 = 6
# rev = 25 - 6 = 19
# chr(19 + ord('a')) = chr(19 + 97) = chr(116) = 't'

# Trace for "z":
# z -> index 25 -> weight 0
# curr = 0
# w = 0 % 26 = 0
# rev = 25 - 0 = 25
# chr(25 + ord('a')) = chr(25 + 97) = chr(122) = 'z'

words2 = ["a", "b", "c"]
weights2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

print("\nwords2 =", words2)
print("weights2 =", weights2)
print("mapWordWeights =", mapWordWeights(words2, weights2))

# Trace for each:
# "a": curr = 1, w = 1, rev = 24, char = 'y'
# "b": curr = 1, w = 1, rev = 24, char = 'y'
# "c": curr = 1, w = 1, rev = 24, char = 'y'
# Result: "yyy"

# Detailed trace for words1
print("\nDetailed trace for words1 = ['abc', 'z']:")
for w in words1:
    curr = 0
    print(f"Word: {w}")
    for c in w:
        idx = ord(c) - ord('a')
        weight = weights1[idx]
        print(f"  char '{c}' -> index {idx}, weight {weight}")
        curr += weight
    print(f"  curr = {curr}")
    w_val = curr % 26
    print(f"  w = curr % 26 = {w_val}")
    rev = 25 - w_val
    print(f"  rev = 25 - w = {rev}")
    char = chr(rev + ord('a'))
    print(f"  char = chr({rev} + ord('a')) = '{char}'")