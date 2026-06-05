from functools import cache
from typing import List

# ----------------------------------------------------------------
# totalWaviness(num1, num2): 
# Compute the total "waviness" of all integers in the range [num1, num2].
#
# Waviness of a number:
#   - Count the number of "peaks" and "valleys" in its digit sequence.
#   - A peak at index i: digits[i-1] < digits[i] > digits[i+1]
#   - A valley at index i: digits[i-1] > digits[i] < digits[i+1]
#   - Total waviness = number of such i in the digit sequence.
#
# Approach:
#   - Use digit DP to compute sum of waviness for all numbers in [0, limit].
#   - Then totalWaviness(num1, num2) = sum_up_to(num2) - sum_up_to(num1).
#   - Finally, add back the waviness of num1 itself (since it was subtracted).
# ----------------------------------------------------------------
def totalWaviness(num1: int, num2: int) -> int:
    """
    Compute total waviness of all integers in [num1, num2].

    Uses:
      - sum_same_len(limit): sum of waviness for all numbers with same length as limit, up to limit.
      - sum_up_to(limit): sum of waviness for all numbers in [0, limit].
      - Then: total = sum_up_to(num2) - sum_up_to(num1) + waviness(num1).
    """

    # ----------------------------------------------------------------
    # sum_same_len(limit):
    # Compute the sum of waviness for all numbers with the same number of digits
    # as `limit`, from the smallest number with that length up to `limit`.
    #
    # Uses digit DP:
    #   dp(i, prev, tight, curr, trend) = total waviness sum for suffix starting at i,
    #     given:
    #       - i: current digit position (0..n-1)
    #       - prev: previous digit
    #       - tight: whether we are still bounded by limit's digits
    #       - curr: current waviness count for this number so far
    #       - trend: direction trend
    #           0: no trend yet
    #           1: increasing (prev < current)
    #           2: decreasing (prev > current)
    #
    #   Returns sum of (final curr) over all valid numbers.
    # ----------------------------------------------------------------
    @cache
    def sum_same_len(limit: int) -> int:
        s = str(limit)
        arr = [int(c) for c in s]
        n = len(arr)

        @cache
        def dp(i: int, prev: int, tight: bool, curr: int, trend: int) -> int:
            """
            Digit DP:
              - i: current position in the digit array
              - prev: previous digit placed
              - tight: are we still constrained by limit's digits?
              - curr: current waviness count for this number
              - trend: 0 (none), 1 (increasing), 2 (decreasing)

            Returns: sum of final waviness counts for all numbers formed from this state.
            """
            if i == n:
                # End of number: return its waviness count
                return curr

            # Maximum digit we can place at this position
            mx = arr[i] if tight else 9
            res = 0

            for d in range(mx + 1):
                # Skip leading zero (numbers must not start with 0)
                if i == 0 and d == 0:
                    continue

                ntight = tight and (d == mx)

                ncurr = curr

                # Update waviness if we form a peak or valley
                if trend == 1 and d < prev:
                    # Previously increasing, now decreasing → peak
                    ncurr += 1
                elif trend == 2 and d > prev:
                    # Previously decreasing, now increasing → valley
                    ncurr += 1

                # Update trend
                if d == prev or i == 0:
                    ntrend = 0
                elif d > prev:
                    ntrend = 1  # increasing
                elif d < prev:
                    ntrend = 2  # decreasing

                res += dp(i + 1, d, ntight, ncurr, ntrend)

            return res

        # Start DP from position 0
        return dp(0, 0, True, 0, 0)

    # ----------------------------------------------------------------
    # sum_up_to(limit):
    # Compute the sum of waviness for all integers in [0, limit].
    #
    # Strategy:
    #   - For each digit length from 1 to (len(limit)-1), sum over all numbers with that length.
    #   - Then sum over numbers with the same length as limit up to limit.
    # ----------------------------------------------------------------
    @cache
    def sum_up_to(limit: int) -> int:
        totald = len(str(limit))
        res = 0

        # Sum over all numbers with fewer digits than limit
        for digits in range(1, totald):
            largest = 10**digits - 1  # e.g., for digits=2, largest=99
            res += sum_same_len(largest)

        # Sum over numbers with the same number of digits as limit, up to limit
        res += sum_same_len(limit)
        return res

    # ----------------------------------------------------------------
    # Main computation:
    #   total = sum_up_to(num2) - sum_up_to(num1) + waviness(num1)
    #
    # Why add waviness(num1)?
    #   - sum_up_to(num1) includes waviness of num1.
    #   - We want range [num1, num2], so we subtract sum_up_to(num1) but then add back waviness(num1).
    # ----------------------------------------------------------------
    res = sum_up_to(num2) - sum_up_to(num1)

    # ----------------------------------------------------------------
    # Add waviness of num1 itself (since it was subtracted in sum_up_to(num1)).
    # Waviness of num1: count peaks and valleys in its digit sequence.
    # ----------------------------------------------------------------
    s = str(num1)
    for i in range(1, len(s) - 1):
        if (s[i - 1] < s[i] > s[i + 1]) or (s[i - 1] > s[i] < s[i + 1]):
            res += 1

    return res


# ----------------------------------------------------------------
# Test cases with inputs inside code (no `if __name__ == "__main__"`)
# ----------------------------------------------------------------
num1_1 = 1
num2_1 = 10
print("num1 =", num1_1)
print("num2 =", num2_1)
print("totalWaviness =", totalWaviness(num1_1, num2_1))

num1_2 = 10
num2_2 = 100
print("\nnum1 =", num1_2)
print("num2 =", num2_2)
print("totalWaviness =", totalWaviness(num1_2, num2_2))

num1_3 = 121
num2_3 = 121
print("\nnum1 =", num1_3)
print("num2 =", num2_3)
print("totalWaviness =", totalWaviness(num1_3, num2_3))
# 121: 1 < 2 > 1 → peak at index 1 → waviness = 1

num1_4 = 123
num2_4 = 123
print("\nnum1 =", num1_4)
print("num2 =", num2_4)
print("totalWaviness =", totalWaviness(num1_4, num2_4))
# 123: 1 < 2 < 3 → no peak/valley → waviness = 0

# Show waviness of a few numbers manually
print("\nManual waviness check:")
def waviness_of_one(n: int) -> int:
    s = str(n)
    cnt = 0
    for i in range(1, len(s) - 1):
        if (s[i - 1] < s[i] > s[i + 1]) or (s[i - 1] > s[i] < s[i + 1]):
            cnt += 1
    return cnt

for x in [1, 10, 11, 12, 21, 121, 123, 132, 212]:
    print(f"x={x}, waviness={waviness_of_one(x)}")