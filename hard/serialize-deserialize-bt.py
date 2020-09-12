# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        if root:
            queue = [root]
            while queue:
                node = queue.pop(0)
                if node:
                    res += str(node.val) + '='
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res += 'null='
        return res[:-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root = []
        if data:
            data = data.split('=')
            root = TreeNode(int(data[0]))
            queue = [root]
            i = 1
            while queue:
                node = queue.pop(0)
                if data[i] != 'null':
                    left = TreeNode(int(data[i]))
                    node.left = left
                    queue.append(node.left)
                i += 1
                if data[i] != 'null':
                    right = TreeNode(int(data[i]))
                    node.right = right
                    queue.append(node.right)
                i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
