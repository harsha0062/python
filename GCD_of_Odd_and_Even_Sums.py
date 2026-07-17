from typing import List
from math import gcd

def gcdOfOddEvenSums(n: int) -> int:
    """
    Return the gcd of:
    - sum of the first n odd numbers
    - sum of the first n even numbers
    """
    sumeven = 0
    sumodd = 0

    # Sum the first 2n positive integers and split by parity
    for i in range(1, n * 2 + 1):
        if i % 2 == 0:
            sumeven += i
        else:
            sumodd += i

    return gcd(sumeven, sumodd)


# Input inside the code
n = 5

print(gcdOfOddEvenSums(n))
