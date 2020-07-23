class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        prev_num = nums[0]
        for num in nums[1:]:
            if num == prev_num:
                nums.remove(num)
            prev_num = num
        return len(nums)
