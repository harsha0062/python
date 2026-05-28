import string

def numberOfSpecialChars(word: str) -> int:
    """
    Count the number of "special" lowercase characters in `word`, where a lowercase
    character c is special if:
      - Both c and c.upper() appear in `word`, and
      - The LAST occurrence of c is BEFORE the FIRST occurrence of c.upper().

    We track:
      - lastlower[c] = index of the last occurrence of lowercase c
      - firstupper[U] = index of the first occurrence of uppercase U

    Then we count lowercase letters c where:
      - c is in lastlower,
      - c.upper() is in firstupper, and
      - lastlower[c] < firstupper[c.upper()].
    """
    n = len(word)
    lastlower = {}   # lowercase char -> last index
    firstupper = {}  # uppercase char -> first index

    # Scan the word once
    for i, c in enumerate(word):
        if c.islower():
            # Update last occurrence for this lowercase character
            lastlower[c] = i
        elif c not in firstupper:
            # Record first occurrence for this uppercase character
            firstupper[c] = i

    # Count special lowercase letters
    count = 0
    for c in string.ascii_lowercase:
        u = c.upper()
        if c in lastlower and u in firstupper and lastlower[c] < firstupper[u]:
            count += 1

    return count


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
word1 = "aaAbcBC"
print("word =", word1)
print("numberOfSpecialChars =", numberOfSpecialChars(word1))

word2 = "abc"
print("\nword =", word2)
print("numberOfSpecialChars =", numberOfSpecialChars(word2))

word3 = "abAb"
print("\nword =", word3)
print("numberOfSpecialChars =", numberOfSpecialChars(word3))

word4 = "AaBbCc"
print("\nword =", word4)
print("numberOfSpecialChars =", numberOfSpecialChars(word4))

# Detailed trace for "aaAbcBC"
print("\nDetailed trace for 'aaAbcBC':")
w = "aaAbcBC"
lastlower = {}
firstupper = {}

for i, c in enumerate(w):
    if c.islower():
        lastlower[c] = i
        print(f"i={i}: c='{c}' (lower) → lastlower[{c}] = {i}")
    else:
        if c not in firstupper:
            firstupper[c] = i
            print(f"i={i}: c='{c}' (upper) → firstupper[{c}] = {i}")
        else:
            print(f"i={i}: c='{c}' (upper) already in firstupper, skip")

print("\nlastlower =", lastlower)
print("firstupper =", firstupper)

count = 0
for c in string.ascii_lowercase:
    u = c.upper()
    cond1 = c in lastlower
    cond2 = u in firstupper
    cond3 = lastlower.get(c, float('inf')) < firstupper.get(u, float('inf'))
    if cond1 and cond2 and cond3:
        count += 1
        print(f"c='{c}' is special: lastlower[{c}]={lastlower[c]} < firstupper[{u}]={firstupper[u]}")
    else:
        print(f"c='{c}': cond1={cond1}, cond2={cond2}, cond3={cond3} → not special")

print("\nFinal count =", count)