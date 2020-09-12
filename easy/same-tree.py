# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preorder(t):
            res = []
            if t:
                queue = [t]
                while queue:
                    node = queue.pop(0)
                    if node:
                        res.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                    else:
                        res.append(None)
            return res
        return preorder(p) == preorder(q)
        
            
