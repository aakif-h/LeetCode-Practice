class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        biggest_count = 0
        count = 0
        for i in range(len(s)):
            uniques = []
            count = 0
            for j in range(i, len(s)):
                if s[j] not in uniques:
                    count += 1
                    uniques.append(s[j])
                    if count > biggest_count:
                        biggest_count = count
                else:
                    break
        

        if count > biggest_count:
            biggest_count = count
        
        return biggest_count
