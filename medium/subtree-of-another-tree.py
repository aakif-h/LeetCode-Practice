# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def traversal(s, t):
            if not s and not t:
                return True
            if s and t and s.val == t.val:
                return traversal(s.left, t.left) and traversal(s.right, t.right)
            return False
        if not s and not t:
            return True
        if not s:
            return False
        if not t:
            return True

        queue = [s]
        while queue:
            node = queue.pop(0)
            if node:
                if node.val == t.val:
                    if traversal(node, t):
                        return True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return False
