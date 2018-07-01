class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #1 97.4p
        from collections import defaultdict
        
        nums_len = len(nums)
        nums_comp = defaultdict()
        
        for i in range(nums_len):
            if nums[i] in nums_comp.keys():
                return [nums_comp[nums[i]], i]
            else:
                nums_comp[target - nums[i]] = i
                
                #1 97.4p
        from collections import defaultdict
        
        """
        #2 slower 87p
        nums_comp = defaultdict()
        
        count = 0
        for num in nums:
            if num in nums_comp.keys():
                return [nums_comp[nums[count]], count]
            else:
                nums_comp[target - num] = count
                
            count += 1
        """
