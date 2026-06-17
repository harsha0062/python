def processStr(s: str, k: int) -> str:
    """
    Process a string with special characters and return a transformed character.

    Special characters:
      - '*': if l > 0, decrement l (represents some kind of "undo" or removal)
      - '#': double l (represents duplication or expansion)
      - '%': no effect on l in the first loop, but in the second loop it transforms k
      - lowercase letters: increment l (representing "add a character")

    Algorithm:
      1. First loop (left to right):
         - Compute the final value of l after applying all operations.
         - l represents the "effective length" or "count" after processing the string.

      2. If k >= l:
         - Return '.' (invalid index or out of bounds).

      3. Second loop (right to left):
         - Reverse the operations to find which original lowercase character
           corresponds to index k.
         - For each character:
             * lowercase: 
                 - if k == l-1, return this character (found the target).
                 - else, decrement l.
             * '*': increment l (reverse of decrement).
             * '#': 
                 - halve l (reverse of doubling).
                 - if k >= l, subtract l from k.
             * '%': transform k = l - 1 - k (mirror index).

      4. Return the found character or '.' if not found.
    """
    l = 0

    # First pass: compute final l
    for c in s:
        if c.islower():
            l += 1
        elif c == '*' and l > 0:
            l -= 1
        elif c == '#':
            l *= 2
        elif c == '%':
            pass  # no effect on l in first pass

    # If k is out of bounds
    if k >= l:
        return '.'

    # Second pass: reverse the operations to find the character at index k
    for c in reversed(s):
        if c.islower():
            if k == l - 1:
                return c
            l -= 1
        elif c == '*':
            l += 1
        elif c == '#':
            l //= 2
            if k >= l:
                k -= l
        elif c == '%':
            k = l - 1 - k

    return '.'


# Test cases with inputs inside code (no `if __name__ == "__main__"`)
s1 = "abc"
k1 = 0
print("s1 =", s1)
print("k1 =", k1)
print("processStr =", processStr(s1, k1))
# l becomes 3 after first pass.
# Reverse: c (l=3, k=0 != 2), l=2; b (l=2, k=0 != 1), l=1; a (l=1, k=0 == 0) → return 'a'

s2 = "abc"
k2 = 1
print("\ns2 =", s2)
print("k2 =", k2)
print("processStr =", processStr(s2, k2))
# Reverse: c (l=3, k=1 != 2), l=2; b (l=2, k=1 == 1) → return 'b'

s3 = "abc"
k3 = 2
print("\ns3 =", s3)
print("k3 =", k3)
print("processStr =", processStr(s3, k3))
# Reverse: c (l=3, k=2 == 2) → return 'c'

s4 = "abc*"
k4 = 0
print("\ns4 =", s4)
print("k4 =", k4)
print("processStr =", processStr(s4, k4))
# First pass: a→1, b→2, c→3, *→2 (l=2)
# Reverse: *→l=3, c (l=3, k=0 != 2), l=2; b (l=2, k=0 != 1), l=1; a (l=1, k=0 == 0) → 'a'

s5 = "ab#c"
k5 = 0
print("\ns5 =", s5)
print("k5 =", k5)
print("processStr =", processStr(s5, k5))
# First pass: a→1, b→2, #→4, c→5 (l=5)
# Reverse: c (l=5, k=0 != 4), l=4; # → l=2, k>=2? 0>=2 false; b (l=2, k=0 != 1), l=1; a (l=1, k=0 == 0) → 'a'

s6 = "a%bc"
k6 = 0
print("\ns6 =", s6)
print("k6 =", k6)
print("processStr =", processStr(s6, k6))
# First pass: a→1, %→1, b→2, c→3 (l=3)
# Reverse: c (l=3, k=0 != 2), l=2; b (l=2, k=0 != 1), l=1; % → k = 1-1-0 = 0; a (l=1, k=0 == 0) → 'a'

# Detailed trace for s5 = "ab#c", k=0
print("\nDetailed trace for s5 = 'ab#c', k=0:")
s = "ab#c"
k = 0
l = 0

print("First pass:")
for c in s:
    if c.islower():
        l += 1
        print(f"  char '{c}' (lower) → l = {l}")
    elif c == '*':
        if l > 0:
            l -= 1
            print(f"  char '*' → l = {l}")
    elif c == '#':
        l *= 2
        print(f"  char '#' → l = {l}")
    elif c == '%':
        print(f"  char '%' → l unchanged = {l}")

print(f"Final l after first pass: {l}")

if k >= l:
    print(f"k >= l, return '.'")
else:
    print(f"Second pass (reverse):")
    for c in reversed(s):
        if c.islower():
            if k == l - 1:
                print(f"  char '{c}' (lower): k == l-1 ({k} == {l-1}) → return '{c}'")
            else:
                print(f"  char '{c}' (lower): k != l-1, l from {l} to {l-1}")
                l -= 1
        elif c == '*':
            print(f"  char '*': l from {l} to {l+1}")
            l += 1
        elif c == '#':
            print(f"  char '#': l from {l} to {l//2}")
            l //= 2
            if k >= l:
                print(f"  k >= l ({k} >= {l}), k from {k} to {k-l}")
                k -= l
        elif c == '%':
            new_k = l - 1 - k
            print(f"  char '%': k from {k} to {new_k}")
            k = new_k