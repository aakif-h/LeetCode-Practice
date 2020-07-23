# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        n = ListNode()
        head = n
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                n.next = ListNode(l1.val)
                l1 = l1.next
            else:
                n.next = ListNode(l2.val)
                l2 = l2.next
            n = n.next
        while l1 != None:
            n.next = ListNode(l1.val)
            n = n.next
            l1 = l1.next
        while l2 != None:
            n.next = ListNode(l2.val)
            n = n.next
            l2 = l2.next
        return head.next
