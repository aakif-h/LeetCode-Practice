# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getLength(node):
            length = 0
            while node:
                node = node.next
                length += 1
            return length
        
        lenA, lenB = getLength(headA), getLength(headB)
        
        turtle = hare = None
        if lenA > lenB:
            hare = headA
            turtle = headB
        else:
            turtle = headA
            hare = headB
        for _ in range(abs(lenA-lenB)):
            hare = hare.next
        while turtle != hare:
            turtle = turtle.next
            hare = hare.next
        return hare
