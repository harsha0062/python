from typing import List

# Function to find the minimum number of boxes needed
def minimumBoxes(apple: List[int], capacity: List[int]) -> int:
    # Total number of apples
    total = sum(apple)
    
    # Sort capacities in descending order (use biggest boxes first)
    capacity.sort(reverse=True)
    
    need = 0  # count of boxes used
    
    # Keep adding boxes until all apples are stored
    while total > 0:
        total -= capacity[need]
        need += 1
    
    return need


# ---------------- INPUT GIVEN INSIDE THE CODE ----------------

apple = [1, 3, 2, 5]       # apples in baskets
capacity = [4, 3, 1, 5]   # box capacities

# Function call
result = minimumBoxes(apple, capacity)

# Output
print("Minimum boxes needed:", result)
