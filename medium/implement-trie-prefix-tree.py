class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.isWord = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self
        for char in word:
            if not char in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self
        for char in word:
            if not char in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self
        for char in prefix:
            if not char in curr.children:
                return False
            curr = curr.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
