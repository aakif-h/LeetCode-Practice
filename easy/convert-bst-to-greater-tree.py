# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def convertBST(self, root: TreeNode) -> TreeNode:
       # if root:
       #     self.convertBST(root.right)
       #     self.total += root.val
       #     root.val = self.total
       #     self.convertBST(root.left)
        stack = []
        node = root
        total = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total
            
            node = node.left
        
        return root
