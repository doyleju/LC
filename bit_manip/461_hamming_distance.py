class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        #1 100p
        z = x ^ y
        
        return bin(z).count('1')
