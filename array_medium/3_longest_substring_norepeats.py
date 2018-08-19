class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_L = 0
        start = 0
        len_s = len(s)
        used = {}
        
        for i in range(len_s):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                max_L = max(max_L, i - start + 1)

            used[s[i]] = i
    
        return max_L
