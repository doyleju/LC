class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        #1 20p
        
        count = 0
        
        while n > 0:
            n &= n - 1
            count += 1
            
        return count
        """
        
        #2 79p
        return bin(n).count('1')
