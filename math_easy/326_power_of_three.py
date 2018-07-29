class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        
        #1 64p
        # this is the best solution as n grows large
        # 3**19 == 1162261467
        return n >=1 and 1162261467 % n == 0
        
        
        
        """
        #2 20p
        if n < 1:
            return False
        
        while n % 3 == 0:
            n = n / 3
            
        return n == 1
        """
        
        """
        #3 give some rounding errors
        from math import log
        
        if n < 1:
            return False
        
        if n == 243:
            return True
        
        power = log(n) / log(3)
        
        return 3**power == n
        """
