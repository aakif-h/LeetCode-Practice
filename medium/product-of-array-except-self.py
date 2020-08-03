class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1 for _ in range(n)]
        right_prod = [1 for _ in range(n)]
        for i in range(1, n):
            left_prod[i] = left_prod[i-1]*nums[i-1]
            right_prod[n-i-1] = right_prod[n-i]*nums[n-i]
        res = [None for _ in range(n)]
        for i in range(n):
            res[i] = left_prod[i]*right_prod[i]
        return res
