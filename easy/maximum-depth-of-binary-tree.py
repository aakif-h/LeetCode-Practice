# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = [[root,1]]
        height = 1
        while queue:
            node, height = queue.pop(0)
            if node.right:
                queue.append([node.right, height+1])
            if node.left:
                queue.append([node.left, height+1])
        return height
