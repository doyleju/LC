class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #1 86p
        """
        #if len(s) != len(t):
        #    return False
        
        from collections import defaultdict
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        for char in s:
            s_dict[char] += 1
        
        for char in t:
            t_dict[char] +=1
            
        if s_dict == t_dict:
            return True
        
        return False
        """
        
        #2 time limit exceeded
        """
        if len(s) != len(t):
            return False
        
        for char in s:
            if s.count(char) != t.count(char):
                return False
            
        return True
        """
        
        #3 95p
        """
        if len(s) != len(t):
            return False
        
        chars = string.ascii_lowercase
        
        for char in chars:
            if s.count(char) != t.count(char):
                return False
            
        return True
        """
        
        #4 47p
        #return sorted(s) == sorted(t)
        
        #5 50p
        from collections import Counter
        return Counter(s) == Counter(t)
