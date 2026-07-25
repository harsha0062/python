from typing import List

def maxProduct(n: int) -> int:
    # Convert the number to a list of its digits
    digits = list(map(int, str(n)))

    # Sort digits in ascending order
    digits.sort()

    # Return the product of the two largest digits
    return digits[-2] * digits[-1]


# Input inside the code
n = 12345

print(maxProduct(n))