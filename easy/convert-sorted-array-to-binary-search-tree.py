# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def constructTree(node, start, end):
            if start > end:
                return None
            mid = (start + end)//2
            
            if not node:
                node = TreeNode(nums[mid])
            
            node.left = constructTree(node.left, start, mid-1)
            node.right = constructTree(node.right, mid+1, end)
            
            return node
        
        return constructTree(None, 0, len(nums)-1)
        
