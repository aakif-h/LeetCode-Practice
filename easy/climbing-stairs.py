class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0]
        arr.append(1)
        arr.append(2)
        
        print(arr)
        
        for i in range(3, n+1):
            arr.append(arr[i - 1] + arr[i - 2])
        
        return arr[n]
