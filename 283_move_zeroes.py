class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        #1 95p
        nums_len = len(nums)
        i = 0
        count = 0
        
        while count < nums_len:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                count += 1
            else:
                i += 1
                count += 1
                
        """
        
        #2 92.5p
        nums_len = len(nums)
        slow = 0
        fast = 1
        
        while fast < nums_len:
            if nums[slow] == 0:
                while nums[fast] == 0 and fast < nums_len - 1:
                    fast +=1
                
                #if nums[fast] > 0: failed 3/21 with this test included
                nums[slow] = nums[fast]
                nums[fast] = 0
                
            slow += 1
            fast += 1
            
        """
