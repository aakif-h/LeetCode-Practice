class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        row = 0
        coins = 1
        while (n - coins >= 0):
            n -= coins
            row += 1
            coins += 1
        return row
