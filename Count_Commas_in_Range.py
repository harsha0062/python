def countCommas(n: int) -> int:
    # Numbers from 1 to 999 do not contain commas
    if n <= 999:
        return 0

    # For every number greater than 999, count the numbers after 999
    return n - 999


# Input inside the code
n = 1500

print(countCommas(n))