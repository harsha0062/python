import string

def numberOfSpecialChars(word: str) -> int:
    """
    Count the number of "special" lowercase characters in `word`.
    A lowercase character c is special if:
        - c is in `word`, and
        - its uppercase version c.upper() is also in `word`.

    Returns the count of such special lowercase letters.
    """
    s = set(word)  # unique characters in word for O(1) membership checks

    # For each lowercase letter a-z, check if both c and c.upper() are in the word
    return sum(1 for c in string.ascii_lowercase if c in s and c.upper() in s)


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
word1 = "aaAbcBC"
print("word =", word1)
print("numberOfSpecialChars =", numberOfSpecialChars(word1))  # Expected: 3 (a, b, c)

word2 = "abc"
print("\nword =", word2)
print("numberOfSpecialChars =", numberOfSpecialChars(word2))  # 0

word3 = "abAb"
print("\nword =", word3)
print("numberOfSpecialChars =", numberOfSpecialChars(word3))  # 1 (a)

word4 = "AaBbCc"
print("\nword =", word4)
print("numberOfSpecialChars =", numberOfSpecialChars(word4))  # 3 (a, b, c)

# Example trace for "aaAbcBC":
print("\nTrace for 'aaAbcBC':")
w = "aaAbcBC"
s = set(w)
print("set(word) =", s)
count = 0
for c in string.ascii_lowercase:
    if c in s and c.upper() in s:
        print(f"  {c} and {c.upper()} both present → count = {count+1}")
        count += 1
print("Final count =", count)