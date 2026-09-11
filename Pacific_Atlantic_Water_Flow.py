from typing import List


# Your function
def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    rows,cols=len(heights),len(heights[0])
    pac,atl=set(),set()
    
    def dfs(i,j,visited,prevheight):
        # Stop DFS if:
        # 1. Cell is already visited
        # 2. Cell is outside the matrix
        # 3. Current height is lower than previous height
        if ((i,j) in visited or 
            i < 0 or i == rows or 
            j < 0 or j == cols or 
            heights[i][j] < prevheight):
            return 
        
        # Mark current cell as reachable
        visited.add((i,j))
        
        # Move down
        dfs(i+1,j,visited,heights[i][j])
        
        # Move up
        dfs(i-1,j,visited,heights[i][j])
        
        # Move right
        dfs(i,j+1,visited,heights[i][j])
        
        # Move left
        dfs(i,j-1,visited,heights[i][j])
    
    # Start DFS from the top row (Pacific)
    # and bottom row (Atlantic)
    for c in range(cols):
        dfs(0,c,pac,heights[0][c])
        dfs(rows-1,c,atl,heights[rows-1][c])

    # Start DFS from the left column (Pacific)
    # and right column (Atlantic)
    for r in range(rows):
        dfs(r,0,pac,heights[r][0])
        dfs(r,cols-1,atl,heights[r][cols-1])
    
    # Store cells that can reach both oceans
    res=[]
    
    for i in range(rows):
        for j in range(cols):
            if (i,j) in pac and (i,j) in atl:
                res.append([i,j])
    
    return res


# ------------------------------------------------
# INPUT
# ------------------------------------------------

heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]


# Call the function
answer = pacificAtlantic(heights)


# Print the result
print("Cells that can reach both Pacific and Atlantic:")
for cell in answer:
    print(cell)