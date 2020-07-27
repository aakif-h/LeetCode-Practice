# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue = [[root,0]]
        while queue:
            node, curr_sum = queue.pop(0)
            if not node.left and not node.right and curr_sum + node.val == sum:
                return True
            if node.left:
                queue.append([node.left, curr_sum + node.val])
            if node.right:
                queue.append([node.right, curr_sum + node.val])
        return False
