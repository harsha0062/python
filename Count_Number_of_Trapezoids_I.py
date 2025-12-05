from collections import defaultdict

# Your original function, unchanged
def countTrapezoids(points):
    point_num = defaultdict(int)
    mod = 10**9 + 7
    ans, total_sum = 0, 0

    # Count the number of points at each y-coordinate
    for point in points:
        point_num[point[1]] += 1

    # For each y-coordinate, calculate the number of edges formed
    for p_num in point_num.values():
        edge = p_num * (p_num - 1) // 2  # Combination: pairs of points on same y
        # Count trapezoids formed with previous levels
        ans = (ans + edge * total_sum) % mod
        # Update total_sum to include new edges
        total_sum = (edge + total_sum) % mod

    return ans

# Example input: list of points
points = [
    [0, 1], [1, 1], [2, 2], [3, 2], [4, 2]  # Modify this as needed for your test cases
]

# Call the function and print the result
result = countTrapezoids(points)
print(result)  # Output the number of trapezoids
