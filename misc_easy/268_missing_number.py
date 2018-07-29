class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        #1 99p
        # Gauss
        max_ = len(nums)
        sum_ = (max_*(max_+1)) // 2
        missing = sum_ - sum(nums)
        
        return missing
        
        
        """
        #2 35p
        full_set = set(range(len(nums)+1))
        missing = full_set - set(nums)
        return missing.pop()
        """
        
        """
        #3  Brute Force
        len_nums = len(nums)
        
        #if len_nums < 2:
        #    return 1
        
        nums.sort()
        
        if nums[0] != 0:
            return 0
        
        if nums[-1] != len_nums:
            return len(nums)
        
        for i in range(1, len_nums):
            #print(i, nums[i])
            if nums[i] != i:
                return i
        """
