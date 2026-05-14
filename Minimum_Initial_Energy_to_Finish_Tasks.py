def minimumEffort(tasks: list[list[int]]) -> int:
    """
    Find minimum initial energy needed to complete all tasks without energy dropping below 0.
    Each task [actualCost, minimumRequired]: after paying actualCost, energy >= minimumRequired.
    Greedy: sort by (minimumRequired - actualCost) descending, process in that order.
    """
    # Sort by "waste" = minimumRequired - actualCost (descending)
    # Tasks needing largest buffer first
    tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
    
    res = 0      # Minimum initial energy needed
    avail = 0    # Available energy after previous tasks
    
    for c, t in tasks:  # actualCost, minimumRequired
        need = t - avail  # Additional energy needed to meet minimum
        if need > 0:
            res += need    # Add to initial energy
            avail += need  # Update available energy
        
        avail -= c    # Spend actual cost
    
    return res


# Test cases with inputs inside code
tasks1 = [[1,2],[2,4],[3,5]]
print("tasks1 =", minimumEffort([[1,2],[2,4],[3,5]]))  # Expected: 4

tasks2 = [[3,2],[4,3],[1,4]]
print("tasks2 =", minimumEffort([[3,2],[4,3],[1,4]]))  # Expected: 6

tasks3 = [[1,1],[1,1]]
print("tasks3 =", minimumEffort([[1,1],[1,1]]))        # Expected: 1

# Visualize greedy sorting + energy flow:
print("\ntasks2=[[3,2],[4,3],[1,4]] processing:")
tasks = [[3,2],[4,3],[1,4]]
tasks.sort(key=lambda x: x[1]-x[0], reverse=True)
print("Sorted by (min-actual) desc:", tasks)  # [[1,4],[4,3],[3,2]]

res, avail = 0, 0
for idx, (c, t) in enumerate(tasks):
    print(f"Task {idx+1}: c={c}, t={t}")
    need = t - avail
    print(f"  avail={avail}, need={max(need,0)}")
    if need > 0:
        res += need
        avail += need
    print(f"  res={res}, spend {c} → avail={avail-c}")
    avail -= c

print(f"Minimum initial energy: {res}")