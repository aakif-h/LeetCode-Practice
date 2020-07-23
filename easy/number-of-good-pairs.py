class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        def choose(a,b):
            denom = fact(b)*fact(a-b)
            return fact(a)//denom
        def fact(x):
            m = [1]
            for i in range(2,x+1):
                m.append(i*m[-1])
            return m[-1]
        
        s = 0
        for val in hash.values():
            if val > 1:
                s += choose(val,2)
        return s
