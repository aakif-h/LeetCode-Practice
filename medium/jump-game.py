class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ind = n-1
        for i in range(ind, -1, -1):
            ind = i if i + nums[i] >= ind else ind
        return ind == 0
