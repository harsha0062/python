class Solution:
    def sumAndMultiply(self, n: int) -> int:
        """
        Concatenate all non-zero digits of n in order,
        then multiply that number by the sum of its digits.
        """
        add = 0
        digit = 0

        for ch in str(n):
            if ch != '0':
                d = int(ch)
                digit = digit * 10 + d
                add += d

        return digit * add


# Test cases inside the code
sol = Solution()

print(sol.sumAndMultiply(1234))    # 1234 * 10 = 12340
print(sol.sumAndMultiply(10203))   # 123 * 6 = 738
print(sol.sumAndMultiply(1000))    # 1 * 1 = 1
print(sol.sumAndMultiply(0))       # 0