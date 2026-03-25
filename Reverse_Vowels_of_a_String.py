def reverseVowels(s: str) -> str:
    """
    Reverse only the vowels in a string using two-pointer technique.
    Vowels: a,e,i,o,u (both lowercase and uppercase).
    Non-vowels stay in their original positions.
    """
    vowels = "aeiouAEIOU"      # All vowels (case-sensitive)
    n = len(s)
    s = list(s)               # Convert to list for in-place swaps
    
    i = 0                     # Left pointer
    j = n - 1                 # Right pointer
    
    while i < j:
        # Both pointers on vowels → swap and move inward
        if s[i] in vowels and s[j] in vowels:
            s[i], s[j] = s[j], s[i]   # Pythonic swap
            i += 1
            j -= 1
        
        # Left is vowel but right isn't → move right pointer left
        elif s[i] in vowels:
            j -= 1
        
        # Right is vowel but left isn't → move left pointer right  
        else:
            i += 1
    
    return "".join(s)         # Convert back to string


# Test cases with inputs inside code
print("s='hello' ->", reverseVowels('hello'))        # 'holle'
print("s='leetcode' ->", reverseVowels('leetcode'))  # 'leotcede'
print("s='IceCreAm' ->", reverseVowels('IceCreAm'))  # 'AceCreIm'
print("s='aA' ->", reverseVowels('aA'))              # 'Aa'

# Visualize step-by-step for "leetcode":
print("\nStep-by-step for 'leetcode':")
s_vis = list('leetcode')
i, j = 0, 7
print(f"Initial: {''.join(s_vis)} (i={i}, j={j})")

while i < j:
    print(f"  s[{i}]='{s_vis[i]}' in vowels? {s_vis[i] in 'aeiouAEIOU'}")
    print(f"  s[{j}]='{s_vis[j]}' in vowels? {s_vis[j] in 'aeiouAEIOU'}")
    
    if s_vis[i] in "aeiouAEIOU" and s_vis[j] in "aeiouAEIOU":
        s_vis[i], s_vis[j] = s_vis[j], s_vis[i]
        print(f"  SWAP: s[{i}]↔s[{j}] → {''.join(s_vis)}")
        i += 1; j -= 1
    elif s_vis[i] in "aeiouAEIOU":
        print(f"  Move j left: {j}→{j-1}")
        j -= 1
    else:
        print(f"  Move i right: {i}→{i+1}")
        i += 1
print(f"Final result: {''.join(s_vis)}")