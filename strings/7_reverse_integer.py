class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 68p
        import re
        
        neg = False
        
        if x < 0:
            neg = True
            x = abs(x)
            
        str_x = str(x)[::-1]
        str_x = re.sub(r'^0+', '', str_x)
        
        str_len = len(str_x)
        multiplier = 1
        current = -1
        new_x = 0
        
        while str_len > 0:
            new_x += int(str_x[current]) * multiplier
            current -= 1
            str_len -= 1
            multiplier *= 10
            
        if new_x > (2**31 -1) or new_x < -(2**31):
            return 0
        
        if neg:
            return -new_x
        else:
            return new_x
