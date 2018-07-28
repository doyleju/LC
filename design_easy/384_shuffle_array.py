#1 85p

class Solution(object):

    from random import random
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.orig = self.nums[:]
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self.orig[:]
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # random.shuffle returns None
        random.shuffle(self.nums)
        return self.nums
