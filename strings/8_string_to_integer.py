class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        #1 99p
        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        
        import re
        
        match = re.search(r'^[-|+]?[0-9]+', str.strip())
        
        if not match:
            return 0
        
        num = int(match.group(0))
        
        if num > INT_MAX:
            return INT_MAX
        
        if num < INT_MIN:
            return INT_MIN
            
        return num
