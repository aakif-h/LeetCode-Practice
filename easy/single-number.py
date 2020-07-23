class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        count_dict = {}
        
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        key = val = 0
        for key,val in count_dict.items():
            if val == 1:
                break
        return key
