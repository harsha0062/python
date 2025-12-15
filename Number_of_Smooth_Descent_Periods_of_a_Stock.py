# Function to count the number of descent periods in the prices list
# A descent period is a contiguous subarray where each element
# is exactly 1 less than the previous element.

def getDescentPeriods(prices):
    # res stores the total number of descent periods
    # Every single element is at least a descent period of length 1
    res = 1

    # count stores the length of the current descent streak
    count = 1

    # Iterate from the second element to the end
    for i in range(1, len(prices)):
        # Check if current element continues the descent
        if (prices[i - 1] - prices[i] == 1):
            # Extend current descent streak
            count += 1
        else:
            # Reset streak if descent is broken
            count = 1

        # Add current streak length to result
        res += count

    return res


# Example input given inside the code
prices = [3, 2, 1, 4]

# Call the function and print the result
ans = getDescentPeriods(prices)
print(ans)
