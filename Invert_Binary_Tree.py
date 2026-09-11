from typing import Optional


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # An empty tree does not need to be inverted
    if root is None:
        return root

    # Recursively invert the left and right subtrees
    left_subtree = invertTree(root.left)
    right_subtree = invertTree(root.right)

    # Swap the inverted subtrees
    root.right = left_subtree
    root.left = right_subtree

    return root


# Input inside the code
root = TreeNode(
    4,
    TreeNode(
        2,
        TreeNode(1),
        TreeNode(3)
    ),
    TreeNode(
        7,
        TreeNode(6),
        TreeNode(9)
    )
)

inverted_root = invertTree(root)

print(inverted_root.val)