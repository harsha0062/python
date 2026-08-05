from typing import List

def findPoisonedDuration(timeSeries: List[int], duration: int) -> int:
    # Store the total poisoned time
    total = 0

    # Add poison time for each attack except the last one
    # If the next attack happens before the current poison ends,
    # only the non-overlapping part is added
    for i in range(len(timeSeries) - 1):
        total += min(timeSeries[i + 1] - timeSeries[i], duration)

    # Add the duration of the last attack
    # Note: this should be added when timeSeries is not empty
    if len(timeSeries) > 0:
        total += duration

    return total


# Input inside the code
timeSeries = [1, 4]
duration = 2

print(findPoisonedDuration(timeSeries, duration))