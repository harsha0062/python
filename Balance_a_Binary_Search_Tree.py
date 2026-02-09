# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balanceBST(root):
    """
    Converts an unbalanced BST into a balanced BST.
    Approach: 
    1. Inorder traversal to get sorted array of values
    2. Recursively build balanced BST using mid-point as root
    """
    nodes = []
    
    # Step 1: Perform inorder traversal to collect sorted values
    def inorder_dfs(node):
        if not node:
            return
        inorder_dfs(node.left)      # Visit left subtree first
        nodes.append(node.val)      # Add current node value (middle order gives sorted list)
        inorder_dfs(node.right)     # Visit right subtree
    
    inorder_dfs(root)
    
    # Step 2: Build balanced BST from sorted array
    def build_balanced_tree(l, r):
        # Base case: no nodes to build
        if l > r:
            return None
        
        # Find middle element to make tree balanced
        mid = l + (r - l) // 2
        root = TreeNode(nodes[mid])  # Middle element becomes root
        
        # Recursively build left subtree with left half
        root.left = build_balanced_tree(l, mid - 1)
        # Recursively build right subtree with right half
        root.right = build_balanced_tree(mid + 1, r)
        
        return root
    
    # Build and return balanced BST
    return build_balanced_tree(0, len(nodes) - 1)

# Input: Create sample unbalanced BST
#       1
#        \
#         2
#        /
#       3
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Convert to balanced BST and print result
balanced_root = balanceBST(root)

# Verify by printing inorder traversal (should be sorted: [1,2,3])
def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.val, end=" ")
        print_inorder(node.right)

print("Balanced BST inorder traversal:")
print_inorder(balanced_root)
print()  # New line
