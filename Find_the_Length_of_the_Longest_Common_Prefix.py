from typing import List

def longestCommonPrefix(arr1: List[int], arr2: List[int]) -> int:
    """
    Find the length of the longest common prefix between any number in arr1 and any number in arr2.

    Approach:
        1. Put all numeric prefixes of numbers in the smaller array (arr1) into a set.
           A prefix here means: for a number 1234, its prefixes are 1234, 123, 12, 1 (by repeatedly dividing by 10).
        2. For each number in arr2, keep removing its least significant digit (n //= 10) until a prefix of it exists in the set.
        3. Track the maximum length (in digits) of such a common prefix.

    Example:
        arr1 = [13, 25, 83, 18], arr2 = [23, 17, 82] → the longest common numeric prefix is 1 → length 1.
    """
    # Use smaller array for prefix set to minimize space
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    prefix_set = set()

    # 1. Precompute all numeric prefixes for arr1
    for n in arr1:
        while n and n not in prefix_set:
            prefix_set.add(n)
            n = n // 10

    res = 0  # longest common prefix length so far

    # 2. For each number in arr2, find its longest prefix that exists in prefix_set
    for n in arr2:
        while n and n not in prefix_set:
            n = n // 10

        # Now n is either 0 or a common prefix (the number itself or a numeric prefix of it)
        if n:
            res = max(res, len(str(n)))

    return res


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
arr1_1 = [1, 10, 100]
arr2_1 = [1000]
print("arr1 =", arr1_1)
print("arr2 =", arr2_1)
print("longest common prefix length =", longestCommonPrefix(arr1_1, arr2_1))  # 4 (1000 and 100 share prefix 1)

arr1_2 = [13, 25, 83, 18]
arr2_2 = [23, 17, 82]
print("\narr1 =", arr1_2)
print("arr2 =", arr2_2)
print("longest common prefix length =", longestCommonPrefix(arr1_2, arr2_2))  # 1

arr1_3 = [100, 200, 300]
arr2_3 = [123, 234, 345]
print("\narr1 =", arr1_3)
print("arr2 =", arr2_3)
print("longest common prefix length =", longestCommonPrefix(arr1_3, arr2_3))  # 1

arr1_4 = [100, 1000]
arr2_4 = [10000, 100000]
print("\narr1 =", arr1_4)
print("arr2 =", arr2_4)
print("longest common prefix length =", longestCommonPrefix(arr1_4, arr2_4))  # 5 (10000)