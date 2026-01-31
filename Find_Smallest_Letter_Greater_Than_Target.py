from typing import List

def nextGreatestLetter(letters: List[str], target: str) -> str:
    """
    Finds the smallest letter in letters that is lexicographically greater than target.
    If no such letter exists, returns the smallest letter in the list (circular search).
    
    Args:
    letters: Sorted list of uppercase letters (no duplicates)
    target: Single character target to find next greatest letter for
    
    Returns:
    The next greatest letter, or the first letter if none found
    """
    for i in letters:
        if i > target:
            return i
    return letters[0]

# Input data - example test cases
letters1 = ["c", "f", "j"]        # Sorted uppercase letters
target1 = "a"                     # Target smaller than all letters

letters2 = ["c", "f", "j"]
target2 = "c"                     # Target equal to first letter

letters3 = ["c", "f", "j"]
target3 = "z"                     # Target larger than all letters

# Test the function with different inputs
print("Test 1: letters=['c','f','j'], target='a'")
print(f"Result: {nextGreatestLetter(letters1, target1)}")  # Expected: 'c'

print("\nTest 2: letters=['c','f','j'], target='c'")
print(f"Result: {nextGreatestLetter(letters2, target2)}")  # Expected: 'f'

print("\nTest 3: letters=['c','f','j'], target='z'")
print(f"Result: {nextGreatestLetter(letters3, target3)}")  # Expected: 'c' (wrap around)
