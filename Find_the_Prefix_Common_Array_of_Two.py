from typing import List

def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
    """
    For each index i, result[i] is the number of common integers
    in the prefixes A[0..i] and B[0..i].

    Uses a frequency array `freq[1..n]`:
        - When an element appears for the first time in A or B, freq[x] = 1.
        - When an element appears for the second time (in the other array),
          freq[x] == 2 → this element is now common in the prefix, so increment `common`.

    Returns an array C where C[i] = count of common integers in prefixes A[0..i] and B[0..i].
    """
    n = len(A)
    result = [0] * n
    # 1‑based: values in A and B are 1..n
    freq = [0] * (n + 1)  # freq[x] counts how many times x has appeared so far
    common = 0            # running count of common elements in current prefix

    for i in range(n):
        # Add A[i] to the current prefix
        freq[A[i]] += 1
        if freq[A[i]] == 2:
            # A[i] has now appeared twice (once in A, once in B) → it is common
            common += 1

        # Add B[i] to the current prefix
        freq[B[i]] += 1
        if freq[B[i]] == 2:
            # B[i] has now appeared twice → it is common
            common += 1

        # Store number of common elements in prefix [0..i] in A and B
        result[i] = common

    return result


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
A1 = [1, 3, 2, 4]
B1 = [3, 1, 4, 2]
print("A =", A1)
print("B =", B1)
print("prefix common array =", findThePrefixCommonArray(A1, B1))
# Expected: [0, 2, 3, 4]

A2 = [1, 2, 3]
B2 = [2, 1, 3]
print("\nA =", A2)
print("B =", B2)
print("prefix common array =", findThePrefixCommonArray(A2, B2))
# Expected: [0, 2, 3]

A3 = [1, 2, 3, 4]
B3 = [4, 3, 2, 1]
print("\nA =", A3)
print("B =", B3)
print("prefix common array =", findThePrefixCommonArray(A3, B3))
# Expected: [0, 0, 2, 4]

# Step‑by‑step trace for A=[1,3,2,4], B=[3,1,4,2]:
print("\nTrace for A=[1,3,2,4], B=[3,1,4,2]:")
freq = [0] * 5  # 0..4; indices 1..4 store counts
common = 0
result = []

for i in range(4):
    a, b = A1[i], B1[i]
    print(f"i={i}: A[i]={a}, B[i]={b}")
    # Process A[i]
    freq[a] += 1
    print(f"  freq[{a}] = {freq[a]}")
    if freq[a] == 2:
        common += 1
        print(f"  → common = {common} (a={a} is common)")

    # Process B[i]
    freq[b] += 1
    print(f"  freq[{b}] = {freq[b]}")
    if freq[b] == 2:
        common += 1
        print(f"  → common = {common} (b={b} is common)")

    result.append(common)
    print(f"  result[{i}] = {common}\n")

print("Final result =", result)