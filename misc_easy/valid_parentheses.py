class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # buggy
        if not s:
            return True
        
        left = { "(", "{", "[" }
        right = { ")", "}", "]" }
        recent = []
        
        for char in s:
            if char in left:
                #print(char)
                recent.append(char)
            elif char in right:
                #print(char)
                #print(recent[-1])
                if str(recent.pop()) != str(char):
                    return False
            else:
                pass
                
        return True
