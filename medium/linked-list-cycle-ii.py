# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        turtle = head.next
        hare = head.next.next
        while hare and hare.next:
            if turtle == hare:
                break
            turtle = turtle.next
            hare = hare.next.next
        if turtle != hare:
            return None
        
        turtle = head
        while turtle != hare:
            turtle = turtle.next
            hare = hare.next
        return hare
