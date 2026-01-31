from typing import List

def replaceElements(arr: List[int]) -> List[int]:
    """
    Replaces each element with the greatest element on its right side.
    The last element is replaced with -1.
    Modifies the array in-place and returns it.
    
    Args:
        arr: List of integers
        
    Returns:
        Modified array where each element is replaced with max of right side
    """
    rightmax = -1  # Maximum value seen from right side (-1 for last element)
    
    # Traverse array from right to left
    for i in range(len(arr)-1, -1, -1):
        newmax = max(rightmax, arr[i])      # Current max including this element
        arr[i] = rightmax                   # Replace with previous max (right side)
        rightmax = newmax                   # Update max for next iteration
    
    return arr

# Test cases with input inside the code
print("Test Case 1:")
arr1 = [17, 18, 5, 4, 6, 1]
result1 = replaceElements(arr1)
print(f"Input:  [17, 18, 5, 4, 6, 1]")
print(f"Output: {result1}")  # Expected: [18, 6, 6, 6, 1, -1]

print("\nTest Case 2:")
arr2 = [400]
result2 = replaceElements(arr2)
print(f"Input:  [400]")
print(f"Output: {result2}")   # Expected: [-1]

print("\nTest Case 3:")
arr3 = [1, 2]
result3 = replaceElements(arr3)
print(f"Input:  [1, 2]")
print(f"Output: {result3}")   # Expected: [2, -1]
