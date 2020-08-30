# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        level = 0
        queue = deque()
        queue.appendleft([root,1])
        if root:
            while queue:
                node,level = queue.pop()
                if not node.left and not node.right:
                    break
                if node.left:
                    queue.appendleft([node.left,level+1])
                if node.right:
                    queue.appendleft([node.right,level+1])
        return level
