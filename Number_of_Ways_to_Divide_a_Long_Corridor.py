# Your given function (unchanged in signature)
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # modulo value
        mod = 10**9 + 7

        # list to store indices of seats
        seats = []

        # collect indices of all seats ('S') in the corridor
        for i, c in enumerate(corridor):
            if c == "S":
                seats.append(i)

        # total number of seats
        length = len(seats)

        # if total seats are fewer than 2 or odd, no valid way
        if length < 2 or length % 2 == 1:
            return 0

        # count valid combinations
        # result initialized to 1 for multiplication
        res = 1

        # start from the second seat index in the seats list
        i = 1

        # iterate over pairs of seat-groups
        # we take gaps between seat[1] & seat[2], seat[3] & seat[4], ...
        while i < length - 1:
            # number of ways to place divider between two seat-groups
            # is the number of positions between these two seats
            res = (res * (seats[i + 1] - seats[i])) % mod

            # jump by 2 to move to the next pair of seat-groups
            i = i + 2

        # final result: total ways modulo 1e9+7
        return res


# Example input inside the code (you can change corridor string to test)
corridor = "SSPPSPS"

# Create an object of Solution to call the method
solution = Solution()

# Call the function and print the result
answer = solution.numberOfWays(corridor)
print(answer)
