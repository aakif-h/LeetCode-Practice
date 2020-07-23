# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output = ListNode(0)
        i = output
        carry = 0
        while l1 is not None or l2 is not None:
            x = l1.val if (l1 is not None) else 0
            y = l2.val if (l2 is not None) else 0
            
            addition = x + y + carry
            carry = addition / 10
            
            i.next = ListNode(addition % 10)
            i = i.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if carry != 0:
            i.next = ListNode(carry)
            
        
        return output.next
            
