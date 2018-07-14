class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        """
        #1 error
        import re
        
        t = re.sub(r'[^a-z0-9]', '', s.lower())
        
        half = len(t) / 2
        
        mid_l = half
        mid_r = -1 - half
        
        left = s[0:mid_l]
        right = s[-1:mid_r]
        
        if left == right:
            return True
        
        return False
        """
        """
        #2 56p
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
                
            while r > l and not s[r].isalnum():
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True
        """
        #3 99p
        import re
        
        t = re.sub(r'[^a-z0-9]', '', s.casefold())
        
        return t == t[::-1]
