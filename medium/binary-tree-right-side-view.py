# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            queue = [[root, 0]]
            while queue:
                node, level = queue.pop(0)
                if len(res) <= level:
                    res.append([node.val])
                else:
                    res[level].append(node.val)
                if node.right:
                    queue.append([node.right, level+1])
                if node.left:
                    queue.append([node.left, level+1])
            for i in range(level+1):
                res[i] = res[i][0]
        return res
