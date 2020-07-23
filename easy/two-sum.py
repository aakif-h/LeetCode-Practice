class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        
        for i in range(len(nums)):
            if target - nums[i] in m:
                return [m[target - nums[i]], i]
            m[nums[i]] = i
        return 'Uh oh how did this happen'
