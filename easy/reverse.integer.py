class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        sign = -1 if (x < 0) else 1
        num = abs(x)
        
        new_num = []
        while num > 0:
            new_num.append(num%10)
            num /= 10
        
        reversed_num = 0
        for i in range(len(new_num)):
            reversed_num += new_num[-1 - i]*10**i
        
        if reversed_num*sign > 2**31-1 or reversed_num*sign < -2**31:
            return 0
        
        return reversed_num*sign
