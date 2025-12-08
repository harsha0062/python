# Method 1: Using boundary adjustment
def countOdds_boundary(low: int, high: int) -> int:
    # If low is even, move it to the next odd
    if (low % 2 == 0):
        low += 1
    # If high is even, move it to the previous odd
    if (high % 2 == 0):
        high -= 1
    # Now low and high are odd; count how many odds are in this inclusive range
    return ((high - low) // 2) + 1


# Method 2: Using direct formula (your function, unchanged)
def countOdds(low: int, high: int) -> int:
    # (high + 1) // 2 = number of odds from 1 to high
    # low // 2         = number of odds from 1 to low - 1
    # Subtracting gives count of odds in [low, high]
    return ((high + 1) // 2) - (low // 2)


# Input inside the code
low = 3
high = 7

# Calling both methods and printing results
print("Using boundary method:", countOdds_boundary(low, high))
print("Using formula method :", countOdds(low, high))
