# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Your original isBalanced function (unchanged)
def height(root):
    if root==None:
        return 0
    l=height(root.left)
    r=height(root.right)
    if abs(l-r)>1 or l==-1 or r==-1:
        return -1
    return 1+max(l,r)

def isBalanced(root):
    return height(root)!=-1

# Input tree construction - balanced binary tree (heights differ by <=1)
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

# Test cases
print("Balanced tree:", isBalanced(root1))  # True

# Input tree construction - unbalanced binary tree (right side too deep)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(3)
root2.right.right.right = TreeNode(4)  # Makes right height=4 vs left=1

print("Unbalanced tree:", isBalanced(root2))  # False

# Single node tree (balanced)
root3 = TreeNode(1)
print("Single node:", isBalanced(root3))  # True

# Empty tree (balanced)
print("Empty tree:", isBalanced(None))  # True
