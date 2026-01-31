from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]: 
    """
    Groups strings that are anagrams of each other.
    
    Anagrams are strings with the same characters and frequencies, just rearranged.
    Uses sorted string as key in hashmap to identify anagrams efficiently.
    
    Args:
        strs: List of strings to group
    
    Returns:
        List of lists where each sublist contains anagrams
    """
    # Dictionary to group anagrams - key: sorted chars, value: list of original strings
    mp = defaultdict(list)

    # Process each string
    for s in strs:
        # Sort characters to create unique key for anagrams
        key = ''.join(sorted(s))
        # Add original string to corresponding anagram group
        mp[key].append(s)
    
    # Extract all anagram groups
    ans = []
    for val in mp.values():
        ans.append(val)
    
    return ans

# Test input directly in code
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Execute and print result
result = groupAnagrams(strs)
print("Grouped Anagrams:")
for i, group in enumerate(result):
    print(f"Group {i}: {group}")

# Expected output:
# Group 0: ['eat', 'tea', 'ate']
# Group 1: ['tan', 'nat']
# Group 2: ['bat']
