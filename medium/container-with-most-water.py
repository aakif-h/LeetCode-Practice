class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        biggest_area = 0
        
        
        short_end = 0
        long_end = len(height) - 1
        while short_end != long_end:
            if biggest_area < (long_end - short_end)*min(height[short_end], height[long_end]):
                biggest_area = (long_end - short_end)*min(height[short_end], height[long_end])
            
            if height[short_end] < height[long_end]:
                short_end += 1
            else:
                long_end -= 1
                
        return biggest_area
