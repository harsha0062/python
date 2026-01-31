
from typing import List


def countSeniors(details: List[str]) -> int:
    """
    Counts the number of seniors (age > 60) from a list of customer details strings.
    
    Each string in details contains age digits at positions -4 to -2 (e.g., "XX60XX" where 60 is age).
    """
    ans = 0  # Counter for seniors
    for s in details:
        age = int(s[-4:-2])  # Extract age from last 4th and 3rd characters from end
        if age > 60:
            ans += 1  # Increment counter for each senior found
    return ans

# Input data - sample customer details with embedded ages
details = [
    "2348712341294",  # age=12
    "22699323481",    # age=93 (senior)
    "4896769658021757", # age=75 (senior)
    "1312131218321",   # age=32
    "2828428482842",   # age=42
    "66733488399911",  # age=99 (senior)
    "99999199911"      # age=19
]

# Test the function and print result
result = countSeniors(details)
print(f"Number of seniors (age > 60): {result}")  # Output: 3
