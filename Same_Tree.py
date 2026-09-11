from typing import Optional


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # If both nodes are empty, the trees match at this position
    if p is None and q is None:
        return True

    # If only one node is empty, the trees are different
    if (p is not None and q is None) or (p is None and q is not None):
        return False

    # Recursively compare the left subtrees
    left_same = isSameTree(p.left, q.left)

    # Recursively compare the right subtrees
    right_same = isSameTree(p.right, q.right)

    # The current nodes and both subtrees must match
    return p.val == q.val and left_same and right_same


# Input inside the code
p = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3)
)

q = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3)
)

print(isSameTree(p, q))