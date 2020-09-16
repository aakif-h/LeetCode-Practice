class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.val = 0
        self.is_word = False

    def insert(self, key: str, val: int) -> None:
        curr = self
        for char in key:
            if not char in curr.children:
                curr.children[char] = MapSum()
            curr = curr.children[char]
        curr.val = val
        curr.is_word = True
            
            
    def sum(self, prefix: str) -> int:
        curr = self
        for char in prefix:
            if not char in curr.children:
                return 0
            curr = curr.children[char]
        
        def dfs(node, total):
            if node.is_word:
                total[0] += node.val
            for child in node.children:
                dfs(node.children[child], total)
            
        total = [0]
        dfs(curr, total)
        return total[0]

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
