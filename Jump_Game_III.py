def canReach(arr: list[int], start: int) -> bool:
    """
    Check if you can reach any index with value 0 from start by jumping:
        i -> i + arr[i] or i -> i - arr[i]
    Uses DFS + visited set to avoid cycles and out‑of‑bounds jumps.
    """
    n = len(arr)
    seen = set()

    def dfs(i: int) -> bool:
        # Terminating conditions
        if i < 0 or i >= n:          # Out of bounds
            return False
        if i in seen:                # Already visited → cycle
            return False
        if arr[i] == 0:              # Found zero → success
            return True

        # Mark current index as visited
        seen.add(i)

        # Try both jumps: i + arr[i] and i - arr[i]
        return dfs(i + arr[i]) or dfs(i - arr[i])

    return dfs(start)


# Test cases with inputs inside code (no if __name__ == "__main__")
print("arr=[4,2,3,0,3,1,2], start=5 ->", canReach([4,2,3,0,3,1,2], 5))  # True
print("arr=[4,2,3,0,3,1,2], start=0 ->", canReach([4,2,3,0,3,1,2], 0))  # True
print("arr=[3,0,2,1,2], start=2 ->", canReach([3,0,2,1,2], 2))          # False
print("arr=[0], start=0 ->", canReach([0], 0))                           # True

# Step‑by‑step trace for arr=[4,2,3,0,3,1,2], start=5
print("\nDFS trace for arr=[4,2,3,0,3,1,2], start=5:")
print("start at index 5 (value 2), jumps to 5+2=7, 5-2=3")
print("7: out of bounds → fail")
print("3: arr[3]=0 → success → return True")