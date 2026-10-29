def countAndSay(n: int) -> str:
    # Start with the first term of the count-and-say sequence
    res = "1"

    # Build terms from 2 through n
    for i in range(1, n):
        # Track the current character being counted
        curr = res[0]

        # Count how many times curr appears consecutively
        count = 1

        # Store the next term
        newdata = ""

        # Traverse the rest of the current term
        for c in res[1:]:
            if c == curr:
                # Continue counting the same character
                count += 1
            else:
                # Add the count and character for the completed group
                newdata += str(count) + curr

                # Start counting the new character
                curr = c
                count = 1

        # Add the final group
        res = newdata + str(count) + curr

    return res


# Input inside the code
n = 5

print(countAndSay(n))