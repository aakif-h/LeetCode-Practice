def houseRobber(nums):
    n = len(nums)
    if not n:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums)
    new_nums = nums
    for i in range(2,n):
        if i - 2 > 0 and nums[i-3] > nums[i-2]:
            new_nums[i] += new_nums[i-3]
        else:
            new_nums[i] += new_nums[i-2]
    return max(new_nums)
