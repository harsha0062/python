from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        # Value stored in the current node
        self.val = val
        # Pointer to the left child
        self.left = left
        # Pointer to the right child
        self.right = right


def maxProduct(root: Optional[TreeNode]) -> int:
    # List to store the sum of every subtree
    all_sums: List[int] = []

    # Helper function to compute subtree sums using postorder traversal
    def tree_sum(node: Optional[TreeNode]) -> int:
        # If node is None, its sum is 0
        if node is None:
            return 0
        # Sum of current subtree = node value + left subtree sum + right subtree sum
        s = node.val + tree_sum(node.left) + tree_sum(node.right)
        # Store this subtree sum in the list
        all_sums.append(s)
        # Return this subtree sum to parent caller
        return s

    # First, compute total sum of the whole tree
    total_sum = tree_sum(root)

    # Variable to keep track of the best (maximum) product
    best = 0
    # Try using each subtree sum as one part of the split
    for s in all_sums:
        # Product = sum of this subtree * sum of the remaining part of the tree
        best = max(best, s * (total_sum - s))

    # Return result modulo 10^9 + 7 as required
    return best % (10**9 + 7)


# ------------------------------------------------------------
# Example: build a sample tree and call maxProduct
# Tree structure (LeetCode example):
#       1
#      / \
#     2   3
#    / \
#   4   5
#
# This corresponds to input: [1,2,3,4,5]
# ------------------------------------------------------------

# Creating nodes
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3)
root = TreeNode(1, node2, node3)

# Call the function and print result
result = maxProduct(root)
print(result)  # Expected output for this example is 110
