# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumRootToLeaf(root):
    res = 0  # Store the final sum of all root-to-leaf binary numbers
    
    def dfs(node, b):
        """
        DFS helper function to build binary number from root to leaf
        node: current tree node
        b: current binary number built so far (passed by reference)
        """
        b <<= 1      # Left shift by 1 (multiply by 2) to make space for current bit
        b |= node.val  # Add current node's value as the least significant bit
        
        # If leaf node (no left or right child), add binary number to result
        if not node.left and not node.right:
            nonlocal res
            res += b
            return 
        
        # Recurse on left child if exists
        if node.left:
            dfs(node.left, b)
        # Recurse on right child if exists  
        if node.right:
            dfs(node.right, b)
    
    dfs(root, 0)  # Start DFS from root with binary number = 0
    return res

# Create sample binary tree input inside the code
# Tree structure:
#       1
#      / \
#     0   1
#    / \   \
#   0   1   0
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.right = TreeNode(0)

# Calculate and print result
result = sumRootToLeaf(root)
print(f"Sum of all root-to-leaf numbers: {result}")  # Output: 22
