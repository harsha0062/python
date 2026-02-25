from typing import List

def sortByBits(arr: List[int]) -> List[int]:
    """
    Sorts the array first by the number of 1 bits (popcount), then by the number itself.
    Uses stable sort: first sort by bit count, then by value.
    """
    arr.sort()                          # Sort by numerical value first (stable sort)
    arr.sort(key=lambda x: x.bit_count())  # Sort by number of 1 bits, maintaining relative order of equal bit counts
    return arr

# Input array directly in the code
arr = [0,1,2,3,4,5,6,7,8]
# Test with another example: [1024,512,256,128,64] also works great!

# Execute the function and print result
result = sortByBits(arr)
print(f"Input: {arr}")
print(f"Output: {result}")
print(f"Bit counts: {[bin(x).count('1') for x in result]}")
