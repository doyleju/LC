class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        """
        #1 2p
        if not needle:
            return 0
        
        import re
        
        match = re.search(needle, haystack)
        
        if not match:
            return -1
        
        return match.start()
        """
        
        """
        #2 error?
            
        needle_length = len(needle)
        
        if needle_length == 0:
            return 0
        
        for char in haystack:
            for i in range(needle_length):
                if char != needle[i]:
                    break
                if i == needle_length - 1:
                    return haystack.index(char)
                
        return -1
        """  
        
        #3 99p
        haystack_length = len(haystack)
        needle_length = len(needle)
        index = 0
        
        if needle_length == 0:
            return 0
        
        while (index + needle_length) <= haystack_length:
            if haystack[index:index+needle_length] == needle:
                return index
            index += 1
        
        #if haystack[index:] == needle:
        #    return index
        
        return -1
