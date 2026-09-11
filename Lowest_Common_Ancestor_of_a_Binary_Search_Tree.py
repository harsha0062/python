# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Your function — unchanged
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    # If both p and q are smaller than root,
    # LCA must be in the left subtree
    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)

    # If both p and q are greater than root,
    # LCA must be in the right subtree
    elif root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)

    # Otherwise, root is the Lowest Common Ancestor
    else:
        return root


# ---------------- INPUT ----------------

# Create the nodes
root = TreeNode(6)

root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)

root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)


# Choose p and q
p = root.left          # Node 2
q = root.left.right    # Node 4


# Find Lowest Common Ancestor
answer = lowestCommonAncestor(root, p, q)


# Print the answer
print("Lowest Common Ancestor:", answer.val)