class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        graph = {}
        
        words.sort(key=len)
        for word in words:
            l = len(word)
            max_cost = 0
            for i in range(l):
                check = word[:i]+word[i+1:]
                if check in graph:
                    max_cost = graph[check] if graph[check] > max_cost else max_cost 
            graph[word] = max_cost+1
        return max(graph.values())
