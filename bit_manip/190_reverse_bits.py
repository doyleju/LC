class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        #1 90p
        reverse_n = '{0:032b}'.format(n)[::-1]
        # convert to int base 2
        return int(reverse_n, 2)
    
        """
        #2
        reversed = 0
        for i in range(32):
            reversed = reversed << 1
            reversed |= (n >> i) & 0x1
        return reversed
        """

        """
        # abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
    
        #3
        # For python, there is no 32bit int, so we need to force it 32 bits.
        n = (n >> 16) | (n << 16) & 0xffffffff
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8) & 0xffffffff
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4) & 0xffffffff
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2) & 0xffffffff
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1) & 0xffffffff
        return n
        """
