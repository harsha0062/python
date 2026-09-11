from typing import List

def kthDistinct(arr: List[str], k: int) -> str:
    # Count the frequency of each string
    count = {}

    for value in arr:
        if value not in count:
            count[value] = 0

        count[value] += 1

    # Traverse the array in its original order
    for value in arr:
        # Process only strings that occur exactly once
        if count[value] == 1:
            k -= 1

        # Return the kth distinct string
        if k == 0:
            return value

    # Return an empty string if fewer than k distinct strings exist
    return ""


# Input inside the code
arr = ["d", "b", "c", "b", "c", "a"]
k = 2

print(kthDistinct(arr, k))