def sumOfGoodIntegers(n: int, k: int) -> int:
    # Store the sum of all compatible integers
    ans = 0

    # Check every integer in the range [n - k, n + k]
    # The lower bound is at least 1
    for i in range(max(1, n - k), n + k + 1):
        # Add i only when n and i have no common set bits
        if (n & i) == 0:
            ans += i

    return ans


# Input inside the code
n = 10
k = 5

print(sumOfGoodIntegers(n, k))