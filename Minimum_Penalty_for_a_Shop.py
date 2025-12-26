# Function kept exactly as you wrote it
def bestClosingTime(customers: str) -> int:
    # minp will store the minimum value of curp seen so far
    minp = 0

    # curp tracks the current "penalty balance"
    # We decrease it for 'Y' (good to stay open) and increase it for 'N' (bad to stay open)
    curp = 0

    # earh will store the earliest hour that gives the minimum penalty
    earh = 0

    # Iterate over each hour in the customers string
    for i in range(len(customers)):
        ch = customers[i]

        # If a customer comes ('Y'), staying open is good, so reduce penalty balance
        if ch == 'Y':
            curp -= 1
        else:
            # If no customer ('N'), staying open is bad, so increase penalty balance
            curp += 1

        # If current balance is less than the minimum seen so far,
        # update the earliest hour and minimum balance
        if curp < minp:
            earh = i + 1   # closing after this hour
            minp = curp

    # Return the earliest hour with minimum penalty
    return earh

# Example inputs to test the function

# Example 1: mix of 'Y' and 'N'
customers1 = "YYNY"
result1 = bestClosingTime(customers1)
print("customers:", customers1, "-> best closing time:", result1)

# Example 2: all 'N' (best to close at hour 0)
customers2 = "NNNNN"
result2 = bestClosingTime(customers2)
print("customers:", customers2, "-> best closing time:", result2)

# Example 3: all 'Y' (best to stay open till the end)
customers3 = "YYYY"
result3 = bestClosingTime(customers3)
print("customers:", customers3, "-> best closing time:", result3)
