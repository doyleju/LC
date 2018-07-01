class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums_len = len(nums)
        
        if nums_len < 2:
            return nums_len
        
        slow = 0
        fast = 1
        
        while fast < nums_len:
            
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]

            fast += 1
        
        return slow + 1
