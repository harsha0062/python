from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Your function (logic NOT changed)
def maxLevelSum(root: Optional[TreeNode]) -> int:
    sum = []  # list to store sum of each level

    def dfs(node, level, sum):
        if node is None:
            return

        # If visiting this level first time, add value
        if len(sum) == level:
            sum.append(node.val)
        else:
            sum[level] += node.val

        # Visit left and right children
        dfs(node.left, level + 1, sum)
        dfs(node.right, level + 1, sum)

    # Start DFS from root at level 0
    dfs(root, 0, sum)

    # Find the level with maximum sum
    max_sum = float("-inf")
    ans = 0

    for i in range(len(sum)):
        if max_sum < sum[i]:
            max_sum = sum[i]
            ans = i + 1   # levels are 1-indexed

    return ans


# ---------------- INPUT (Tree Construction) ----------------
# Example tree:
#        1
#       / \
#      7   0
#     / \
#    7  -8

root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)

# Call function and print output
result = maxLevelSum(root)
print("Level with maximum sum:", result)
