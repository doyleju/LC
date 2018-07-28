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
        #return bin(n).count('1')
    
        #3 79p
        mask = 1
        bits = 0
        
        for i in range(32):
            #n = n & mask
            if n & mask != 0:
                bits += 1
                
            mask = mask << 1
                
        return bits
