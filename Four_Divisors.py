# Function to compute the sum of divisors for numbers
# that have exactly four divisors
# NOTE: This function body is kept exactly as you provided

from typing import List

def sumFourDivisors(nums: List[int]) -> int:
    total = 0
    # Iterate over each number in the list
    for num in nums:
        count = 0   # To count the number of divisors
        div = 0     # To store the sum of divisors

        # Check divisors from 1 to sqrt(num)
        for i in range(1, int(num ** 0.5) + 1):
            # If i is a divisor of num
            if num % i == 0:
                count += 1      # Count divisor i
                div += i        # Add divisor i to sum

                # Check the paired divisor num // i
                # Only add if i and num//i are different (i*i != num)
                if i * i != num:
                    count += 1          # Count paired divisor
                    div += num // i     # Add paired divisor to sum

                # If divisors become more than 4, break early
                if count > 4:
                    break

        # If the number has exactly 4 divisors, add its divisor sum to total
        if count == 4:
            total += div

    # Return the final total sum of divisors for all valid numbers
    return total


# ---------- Input and Output Section ----------

# You can change this list to test with other inputs
nums = [21, 4, 7]   # Example input list

# Call the function with the input list
answer = sumFourDivisors(nums)

# Print the result
print("Input array:", nums)
print("Sum of divisors of numbers having exactly four divisors:", answer)
