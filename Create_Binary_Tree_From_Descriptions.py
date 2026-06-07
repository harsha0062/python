from typing import List, Optional
from collections import defaultdict, deque

# ----------------------------------------------------------------
# TreeNode definition (as given in the problem statement)
# ----------------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ----------------------------------------------------------------
# createBinaryTree(descriptions):
# Build a binary tree from a list of parent-child-direction descriptions.
#
# Each description is [parent, child, isLeft]:
#   - parent: parent node value
#   - child: child node value
#   - isLeft: 1 if child is left child, 0 if right child
#
# Assumptions:
#   - All node values are unique.
#   - The descriptions form a valid binary tree.
#   - There is exactly one root (a node that is never a child).
#
# Algorithm:
#   1. Build adjacency list: adj[parent] = list of (child, isLeft).
#   2. Track all children in a set.
#   3. Find root: the node that is not in the children set.
#   4. Build the tree using BFS starting from the root:
#        - For each node, look up its children in adj[node.val].
#        - Create child TreeNode(s) and attach them as left/right.
#        - Push children to the queue.
#   5. Return the root TreeNode.
# ----------------------------------------------------------------
def createBinaryTree(descriptions: List[List[int]]) -> Optional[TreeNode]:
    root = 0
    children = set()
    adj = defaultdict(list)

    # Step 1: Build adjacency list and track all children
    for p, c, il in descriptions:
        children.add(c)
        adj[p].append((c, il))

    # Step 2: Find the root (node that is never a child)
    for p, c, il in descriptions:
        if p not in children:
            root = p
            break

    # Step 3: Create root node and build the tree using BFS
    res = TreeNode(root)
    q = deque([res])

    while q:
        node = q.popleft()

        # Attach children according to adjacency list
        for ch, il in adj[node.val]:
            child = TreeNode(ch)
            if il:
                node.left = child
            else:
                node.right = child
            q.append(child)

    return res


# ----------------------------------------------------------------
# Test cases with inputs inside code (no `if __name__ == "__main__"`)
# ----------------------------------------------------------------
descriptions1 = [
    [20, 15, 1],
    [20, 17, 0],
    [50, 20, 1],
    [50, 80, 0],
    [80, 19, 1]
]
print("descriptions1 =", descriptions1)
root1 = createBinaryTree(descriptions1)

# Helper to print tree in level order (for verification)
def print_tree_level_order(root: Optional[TreeNode]) -> None:
    if not root:
        print("[]")
        return
    q = deque([root])
    vals = []
    while q:
        node = q.popleft()
        if node:
            vals.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            vals.append(None)
    # Trim trailing None
    while vals and vals[-1] is None:
        vals.pop()
    print(vals)

print("Tree level order (descriptions1):", print_tree_level_order(root1))

descriptions2 = [
    [1, 2, 1],
    [1, 3, 0]
]
print("\ndescriptions2 =", descriptions2)
root2 = createBinaryTree(descriptions2)
print("Tree level order (descriptions2):", print_tree_level_order(root2))

descriptions3 = [
    [1, 2, 1]
]
print("\ndescriptions3 =", descriptions3)
root3 = createBinaryTree(descriptions3)
print("Tree level order (descriptions3):", print_tree_level_order(root3))