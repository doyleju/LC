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
    
        """
        # Site Solution
        # Note overflow prevention?
        public int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
        }
        """
