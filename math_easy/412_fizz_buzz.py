class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        nums = []
        
        for num in range(1, n+1):
            
            this_num = str(num)
            fizz = ''
            buzz = ''
            
            if num % 3 == 0:
                fizz = 'Fizz'
                this_num = ''
                
            if num % 5 == 0:
                buzz = 'Buzz'
                this_num = ''
                
            nums.append('{}{}{}'.format(this_num, fizz, buzz))
        
        return nums
