# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        
        res = []
        while queue != []:
            total_sum = count = 0
            temp = []
            while queue != []:
                n = queue.pop(0)
                total_sum += n.val
                count += 1
                if n.left != None:
                    temp.append(n.left)
                if n.right != None:
                    temp.append(n.right)
            queue = temp
            res.append(total_sum/count)
        return res
    
