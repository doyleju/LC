class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #1 94p
        start = 1
        end = n
        lowest_bad = n
        mid = (end + start) // 2
        
        while start <= end:
            if isBadVersion(mid):
                end = mid -1
                lowest_bad = mid
            else:
                start = mid + 1
                
            mid = (start + end) // 2
            
        return lowest_bad
