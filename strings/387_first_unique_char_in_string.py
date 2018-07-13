class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # 70p
        
        from collections import defaultdict
        
        counts = defaultdict(int)
        positions = defaultdict(int)
        
        i = 0
        
        for char in s:
            counts[char] += 1
            #positions[char].append(i)
            #positions[char] = i
            #i += 1
            
        #for i, char in enumerate(list(s)):
        #    if counts[char] == 1:
        #        return i
         
        for char in s:
            if counts[char] == 1:
                return i
            i += 1
        
        return -1

        
        #2 68p
        """
        from collections import Counter
        
        counts = Counter(s)
        
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
            
        return -1
        """
