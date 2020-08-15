class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for __ in range(n)]
        
        topleft = 0
        topright = n-1
        bottomleft = 0
        bottomright = n-1
        
        right = True
        left = up = down = False
        
        r,c = 0,0
        for e in range(1,n**2+1):
            matrix[r][c] = e
            if right:
                if c == topright:
                    right = False
                    down = True
                    topleft += 1
                    r += 1
                else:
                    c += 1
            elif down:
                if r == bottomright:
                    down = False
                    left = True
                    topright -= 1
                    c -= 1
                else:
                    r += 1
            elif left:
                if c == bottomleft:
                    left = False
                    up = True
                    bottomright -= 1
                    r -= 1
                else:
                    c -= 1
            else:
                if r == topleft:
                    up = False
                    right = True
                    bottomleft += 1
                    c += 1
                else:
                    r -= 1
        return matrix
