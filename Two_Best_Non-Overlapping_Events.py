from typing import List

def maxTwoEvents(events: List[List[int]]) -> int:
    # This list will store time points
    # (time, type, value)
    # type = 1 → event start
    # type = 0 → event end
    times = []

    # Convert each event into start and end markers
    for e in events:
        # Event start
        times.append((e[0], 1, e[2]))
        # Event end (end + 1 ensures no overlap)
        times.append((e[1] + 1, 0, e[2]))

    ans = 0        # Stores final maximum answer
    max_value = 0 # Best value of an event that already ended

    # Sort by time
    times.sort()

    # Process each time point
    for time_value in times:
        # If it is a start of an event
        if time_value[1] == 1:
            # Try combining this event with the best previous event
            ans = max(ans, time_value[2] + max_value)
        else:
            # Update max_value when an event ends
            max_value = max(max_value, time_value[2])

    return ans


# ---------------- INPUT GIVEN INSIDE CODE ----------------

events = [
    [1, 3, 4],
    [2, 4, 3],
    [3, 5, 1],
    [6, 7, 5]
]

# Call the function
result = maxTwoEvents(events)

# Output
print("Maximum value from at most two events:", result)
