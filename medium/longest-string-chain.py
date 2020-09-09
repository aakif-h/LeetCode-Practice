class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        graph = {}
        for word in sorted(words, key=len):
            l = len(word)
            costs = [0]
            for i in range(l):
                check = word[:i]+word[i+1:]
                if check in graph:
                    costs.append(graph[check]) 
            graph[word] = max(costs)+1
        return max(graph.values())
        
