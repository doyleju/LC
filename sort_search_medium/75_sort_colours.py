class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        """
        #1 buggy
        slow = 0
        fast = slow + 1
        colour = 0
        len_nums = len(nums)
        
        while slow < len_nums - 1:
            
            while nums[slow] == colour and slow < len_nums - 1:
                slow +=1
            
            fast = slow + 1
                
            while fast < len_nums and slow < len_nums - 1:
                if nums[fast] == colour:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    break
                    
                if fast == len_nums - 1:
                    colour += 1
                    fast = slow
                    
                fast += 1
                
            slow += 1
            
        """
        
        #2 79p
        # 3 way partition algorithm
        value = 1
        high = len(nums) - 1
        low = mid = 0
        
        while mid <= high:
            if nums[mid] < value:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            elif nums[mid] == value:
                mid += 1
            else: # nums[mid] > value
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
