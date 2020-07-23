class Solution:
    def isHappy(self, n: int) -> bool:
        check_dict = {n:1}
        while n != 1:
            n = sum_square_digits(n)
            if n in check_dict:
                return False
            check_dict[n] = 1
        return True
    
    
def sum_square_digits(num):
    sum_squares = 0
    while num != 0:
        sum_squares += (num%10)**2
        num = num//10
    return sum_squares
