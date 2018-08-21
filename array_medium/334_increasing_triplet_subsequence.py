class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        import bisect
        inc = [float('inf')] * 2
        for x in nums:
            i = bisect.bisect_left(inc, x)
            if i >= 2:
                return True
            inc[i] = x
            #print(inc)
        return False
        """
    
        if not nums or len(nums) < 3:
            return False
        min1, min2 = float('inf'), float('inf')
        for val in nums:
            if val > min2:
                return True
            if val < min1:
                min1 = val
            if val > min1 and val < min2:
                min2 = val
        return False
