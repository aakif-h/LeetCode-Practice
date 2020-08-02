class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visitedIndices = [-1 for _ in range(128)]
        start_index = 0
        res = 0
        for i in range(len(s)):
            start_index = max(visitedIndices[ord(s[i])]+1, start_index)
            res = max(i - start_index + 1, res)
            visitedIndices[ord(s[i])] = i
        return res
