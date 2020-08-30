class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        check = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            j = i+1
            k = n-1
            while (j < k):
                triple = (nums[i], nums[j], nums[k])
                total = nums[i] + nums[j] + nums[k]
                #print(total, i, nums[i], j, nums[j], k, nums[k])
                if not triple in check and total == 0:
                    check.add(triple)
                if total <= 0:
                    j += 1
                if total >= 0:
                    k -= 1
        return list(check)
