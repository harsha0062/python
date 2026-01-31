from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    """
    Finds the longest common prefix among an array of strings.
    Compares character by character across all strings using first string as reference.
    """
    res = ""  # Result prefix being built
    
    # Iterate through each character position of first string
    for i in range(len(strs[0])):
        # Check ALL strings at current position i
        for s in strs:
            # If string ends before position i OR character doesn't match
            if i == len(s) or s[i] != strs[0][i]:
                return res  # Return current prefix (mismatch found)
        # If all strings match at position i, add character to result
        res += strs[0][i]
    
    return res  # All characters matched till end

# Test input data
strs1 = ["flower","flow","flight"]      # Expected: "fl"
strs2 = ["dog","racecar","car"]         # Expected: ""  
strs3 = ["interspecies","interstellar","interstate"]  # Expected: "inters"
strs4 = ["a"]                           # Expected: "a"
strs5 = [""]                            # Expected: ""

# Test cases with output
print(f"Input: {strs1}")
print(f"Output: '{longestCommonPrefix(strs1)}'")  # "fl"

print(f"\nInput: {strs2}")
print(f"Output: '{longestCommonPrefix(strs2)}'")  # ""

print(f"\nInput: {strs3}")
print(f"Output: '{longestCommonPrefix(strs3)}'")  # "inters"

print(f"\nInput: {strs4}")
print(f"Output: '{longestCommonPrefix(strs4)}'")  # "a"
