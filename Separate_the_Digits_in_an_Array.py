def separateDigits(nums: list[int]) -> list[int]:
    """
    Separate each digit of each number and return as flat list in original order.
    Process numbers backward, extract digits right-to-left, then reverse final result.
    """
    ans = []
    
    # Process numbers from last to first
    for i in range(len(nums)-1, -1, -1):
        x = nums[i]               # Current number
        
        # Extract digits from right to left (units, tens, hundreds...)
        while x > 0:
            ans.append(x % 10)    # Get least significant digit
            x = x // 10           # Remove last digit
        
        # Skip x=0 (no digits to add)
    
    ans.reverse()                 # Reverse to get original order
    return ans


# Test cases with inputs inside code
print("nums=[12,345] ->", separateDigits([12,345]))           # [1,2,3,4,5]
print("nums=[7] ->", separateDigits([7]))                     # [7]
print("nums=[4321,964] ->", separateDigits([4321,964]))       # [4,3,2,1,9,6,4]
print("nums=[0,0] ->", separateDigits([0,0]))                 # [] (0 contributes no digits)

# Visualize digit extraction:
print("\nDigit extraction for nums=[12,345]:")
nums = [12, 345]
ans = []

for i in range(len(nums)-1, -1, -1):
    print(f"Number {nums[i]}:")
    x = nums[i]
    while x > 0:
        digit = x % 10
        print(f"  {x} % 10 = {digit}, append {digit}")
        ans.append(digit)
        x = x // 10
    print()

print("ans before reverse:", ans)
ans.reverse()
print("ans after reverse: ", ans)