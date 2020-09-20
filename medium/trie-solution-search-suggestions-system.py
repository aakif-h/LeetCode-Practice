class Trie:

    def __init__(self):
        self.children = {}
        self.is_word = False
        self.string = ""
    
    
    def insert(self, word):
        curr = self
        for char in word:
            if not char in curr.children:
                curr.children[char] = Trie()
                curr.children[char].string = curr.string + char
            curr = curr.children[char]
        curr.is_word = True

    
class Solution:
    
    def __init__(self):
        self.matches = None
    
    
    def dfs(self, trie):
        if len(self.matches) == 3:
            return
        if trie.is_word:
            self.matches.append(trie.string)
        for child in trie.children:
            self.dfs(trie.children[child])
    
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()
        for product in products:
            trie.insert(product)
        
        res = []
        for char in searchWord:
            self.matches = []
            if char in trie.children:
                self.dfs(trie.children[char])
                trie = trie.children[char]
            res.append(self.matches)
        return res 
        '''
        ====================
        BRUTE FORCE SOLUTION
        ====================
        n = len(searchWord)
        products.sort()
        res = []
        for i in range(n):
            row = []
            count = 0
            for product in products:
                if count < 3 and searchWord[:i+1] == product[:i+1]:
                    row.append(product)
                    count += 1
            res.append(row)
        return res'''
