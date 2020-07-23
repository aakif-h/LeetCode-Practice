class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        is_first_char = True
        sign = 1
        num = []
        for i in range(len(str)):
            if is_first_char == True and str[i] == ' ':
                continue
                
            if is_first_char == True:
                if str[i] == '-':
                    sign = -1
                    is_first_char = False
                    continue
                    
                if str[i] == '+':
                    is_first_char = False
                    continue
            
            
            if ord(str[i]) >= 48 and ord(str[i]) <= 57:
                num.append(ord(str[i]) - 48)
                is_first_char = False
            else:
                break
        
        n = 0
        for i in range(len(num)):
            n += num[-1 - i]*10**i
            
        if sign*n > 2**31-1:
            return 2**31 - 1
        if sign*n < -2**31:
            return -2**31
        
        return sign*n
