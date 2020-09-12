# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            queue = [[root,float("-inf"),float("inf")]]
            while queue:
                node,lower,upper = queue.pop()
                if node.val <= lower or node.val >= upper:
                    return False
                if node.left:
                    queue.append([node.left, lower, node.val])
                if node.right:
                    queue.append([node.right, node.val, upper])
        return True
