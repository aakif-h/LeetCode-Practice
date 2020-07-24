# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def getHeight(root):
            r = l = 1
            if root.left != None:
                l += getHeight(root.left)
            if root.right != None:
                r += getHeight(root.right)
            return max(l,r)
        
        sum_list = [0 for _ in range(getHeight(root))]
        count_list = [0 for _ in range(len(sum_list))]
        def getTotalSumByLevel(root, level):
            sum_list[level] += root.val
            count_list[level] += 1
            if root.right != None:
                getTotalSumByLevel(root.right, level+1)
            if root.left != None:
                getTotalSumByLevel(root.left, level+1)
        getTotalSumByLevel(root, 0)
        
        avg_list = []
        for i in range(len(sum_list)):
            avg_list.append(sum_list[i]/count_list[i])
        return avg_list
