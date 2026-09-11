from typing import List

def dailyTemperatures(temp: List[int]) -> List[int]:
    # Initialize the result with 0 for each temperature
    res = [0] * len(temp)

    # Store pairs of [temperature, index]
    # Temperatures in the stack remain in decreasing order
    stack = []

    # Traverse all temperatures
    for i, t in enumerate(temp):
        # Resolve previous temperatures when a warmer temperature is found
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd

        # Add the current temperature and its index to the stack
        stack.append([t, i])

    # Return the number of days to wait for each temperature
    return res


# Input inside the code
temp = [73, 74, 75, 71, 69, 72, 76, 73]

print(dailyTemperatures(temp))