class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        #1 88p
        from collections import defaultdict
        
        anagrams = defaultdict(list)
        
        for string in strs:
            sorted_string = ''.join(sorted(string))
            anagrams[sorted_string].append(string)
            
        #result = []
        
        #for string_list in anagrams.values():
        #    result.append(string_list)
            
        #return result
        return [v for v in anagrams.values()]
