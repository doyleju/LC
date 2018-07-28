class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #1 40p
        # kadane's algorithm 
        
        len_nums = len(nums)
        
        if len_nums < 2:
            return nums[0]
        
        max_curr = nums[0]
        max_sofar = max_curr
        
        for i in range(1, len_nums):
            max_curr = max(nums[i], nums[i] + max_curr)
            max_sofar = max(max_sofar, max_curr)
            
        return max_sofar
