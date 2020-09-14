# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = deque()
        if root:
            level = 0       
            queue = deque()
            queue.appendleft([root,level])
            while queue:
                node,level = queue.pop()
                if node:
                    if len(res) <= level:
                        res.appendleft([node.val])
                    else:
                        res[-1 - (level)].append(node.val)
                    queue.appendleft([node.left,level+1])
                    queue.appendleft([node.right,level+1])
        return res
