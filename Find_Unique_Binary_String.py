def findDifferentBinaryString(nums: list[str]) -> str:
    """
    Find a binary string of length n that doesn't exist in given list of n unique binary strings.
    Uses diagonal XOR trick: flip diagonal elements to guarantee uniqueness (pigeonhole principle).
    """
    ans = []
    
    # For each position i, look at nums[i][i] (diagonal element)
    # Flip it: if nums[i][i] == '0' then use '1', else use '0'
    for i in range(len(nums)):
        curr = nums[i][i]      # Get diagonal char
        ans.append("1" if curr == "0" else "0")  # Flip it
    
    # Join to form the result string
    return "".join(ans)


# Test cases with inputs inside code
nums1 = ["01", "10"]
print("nums=", nums1, "->", findDifferentBinaryString(nums1))  # Expected: "11" or "00"

nums2 = ["00", "01"]
print("nums=", nums2, "->", findDifferentBinaryString(nums2))  # Expected: "11" or "10"

nums3 = ["1110", "1101", "0110", "0011"]
print("nums=", nums3, "->", findDifferentBinaryString(nums3))  # Expected: "1010"

nums4 = ["10", "0"]
print("nums=", nums4, "->", findDifferentBinaryString(nums4))  # Expected: "11" or "01"
