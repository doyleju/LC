class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Fibonicci type
        # a is num ways to reach curr step, b is num ways to reach next step
        
        """
        #1 99p
        a = b = 1
        
        for _ in range(n):
            a, b = b, a+b
            
        return a
        """
        
        #2 99p
        
        result = [0, 1, 2]
        
        for i in range(3, n+1, 1):
            result.append(result[i-1] + result[i-2])
            
        return result[n]
