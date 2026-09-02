from typing import List

def combinationSum3(k: int, n: int) -> List[List[int]]:
    res = []

    def comb(curr, k, n, start):
        # If we have chosen k numbers and their sum is n, store the combination
        if k == 0 and n == 0:
            res.append(curr)

        # Stop if we have already used k numbers
        if k <= 0:
            return

        # Try all numbers from start to 9 (or n, whichever is smaller)
        for i in range(start, min(10, n + 1)):
            comb(curr + [i], k - 1, n - i, i + 1)

    # Start the backtracking with an empty combination
    comb([], k, n, 1)

    return res


# Input inside the code
k = 3
n = 7

print(combinationSum3(k, n))