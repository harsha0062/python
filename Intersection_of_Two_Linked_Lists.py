# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# User's original function - finds intersection node of two linked lists
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    """
    Two-pointer technique to find intersection point.
    Both pointers traverse their lists, then switch to the other list when reaching end.
    This equalizes path lengths so they meet at intersection (or None if no intersection).
    Time: O(A+B), Space: O(1) [web:1][web:5]
    """
    l1, l2 = headA, headB
    while l1 != l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA
    return l1

# Create test case: ListA: 4->1->8->4->5, ListB: 5->6->1->8->4->5 (intersect at 8)
# Build ListA
node4a = ListNode(4)
node1 = ListNode(1)
node8 = ListNode(8)
node4b = ListNode(4)
node5 = ListNode(5)
node4a.next = node1
node1.next = node8
node8.next = node4b
node4b.next = node5
headA = node4a

# Build ListB (shares nodes from 8 onwards)
node5b = ListNode(5)
node6 = ListNode(6)
node5b.next = node6
node6.next = node1  # intersection starts here
headB = node5b

# Find and print intersection
intersection = getIntersectionNode(headA, headB)
print("Intersection node value:", intersection.val if intersection else "None")
