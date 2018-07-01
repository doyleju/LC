class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #1 95p
        return 2*sum(set(nums)) - sum(nums)
        
        #2 95p
        #from collections import Counter
        #counts = Counter(nums)
        #for value, count in counts.items():
        #    if count < 2:
        #        return value
            
        #3 70p
        #from collections import defaultdict
        #this_dict = defaultdict(int)
        #for num in nums:
        #    this_dict[num] += 1 
        
        #for key, count in this_dict.items():
        #    if count < 2:
        #        return key
