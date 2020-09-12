class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_streak = 0
        for num in nums:
            streak = 1
            curr = num
            while curr+1 in s:
                streak += 1
                curr += 1
            max_streak = max(streak, max_streak)
        return max_streak
