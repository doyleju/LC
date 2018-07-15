class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        
        #1 99p
        columns = zip(*strs)
        
        str_ret = ""
        
        for _, column in enumerate(columns):
            if len(set(column)) == 1:
                str_ret += column[0]
            else:
                break
                
        return str_ret
    
    
        """    
        #2 89p
        columns = zip(*strs)
        
        str_ret = ""
        
        for column in columns:
            if len(set(column)) == 1:
                str_ret += column[0]
            else:
                break
                
        return str_ret
        """
