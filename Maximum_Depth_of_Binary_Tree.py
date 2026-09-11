from typing import Optional


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    # An empty tree has a depth of 0
    if root is None:
        return 0

    # Recursively calculate the depth of the left subtree
    left_depth = maxDepth(root.left)

    # Recursively calculate the depth of the right subtree
    right_depth = maxDepth(root.right)

    # Current depth is one more than the deeper subtree
    return 1 + max(left_depth, right_depth)


# Input inside the code
root = TreeNode(
    1,
    TreeNode(2, TreeNode(4), TreeNode(5)),
    TreeNode(3)
)

print(maxDepth(root))