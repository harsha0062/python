from typing import List

def hitBricks(grid: List[List[int]], hits: List[List[int]]) -> List[int]:
    # Get the number of rows and columns
    rows, cols = len(grid), len(grid[0])

    # Directions for moving up, down, left, and right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def index(r, c):
        # Convert a 2D position into a 1D index
        return r * cols + c

    def is_valid(r, c):
        # Check whether a position is inside the grid
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c):
        # Stop if the position is invalid or is not an active brick
        if not is_valid(r, c) or grid[r][c] != 1:
            return 0

        # Mark the brick as stable and visited
        grid[r][c] = 2
        size = 1

        # Visit all neighboring bricks
        for dr, dc in directions:
            size += dfs(r + dr, c + dc)

        return size

    def is_connected_to_top(r, c):
        # A brick in the first row is connected to the top
        # Otherwise, check whether it touches a stable brick
        return r == 0 or any(
            grid[r + dr][c + dc] == 2
            for dr, dc in directions
            if is_valid(r + dr, c + dc)
        )

    def union_find():
        # Initialize the parent and component-size arrays
        parent = list(range(rows * cols + 1))
        size = [1] * (rows * cols + 1)

        def find(x):
            # Find the root with path compression
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):
            # Find the roots of both nodes
            root_x, root_y = find(x), find(y)

            # Merge the components if they are different
            if root_x != root_y:
                if size[root_x] > size[root_y]:
                    parent[root_y] = root_x
                    size[root_x] += size[root_y]
                else:
                    parent[root_x] = root_y
                    size[root_y] += size[root_x]

        def union_top():
            # Connect all top-row bricks to the virtual top node
            for c in range(cols):
                if grid[0][c] == 1:
                    union(index(0, c), rows * cols)

        return find, union, size, union_top

    # Remove every brick affected by a hit
    for r, c in hits:
        grid[r][c] -= 1

    # Mark all bricks that remain connected to the top
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and is_connected_to_top(r, c):
                dfs(r, c)

    result = []

    # Add hits back in reverse order
    for r, c in reversed(hits):
        grid[r][c] += 1

        # If the restored brick connects to the top,
        # count the newly stable bricks excluding the restored brick
        if grid[r][c] == 1 and is_connected_to_top(r, c):
            result.append(dfs(r, c) - 1)
        else:
            result.append(0)

    # Reverse the results to match the original hit order
    return result[::-1]


# Input inside the code
grid = [
    [1, 0, 0, 0],
    [1, 1, 1, 0]
]
hits = [[1, 0]]

print(hitBricks(grid, hits))