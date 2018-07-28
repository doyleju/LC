# 95p without any checks on stack before pop, top, getMin
# 25p with checks !

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = [2147483648]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.mins[-1]:
            self.mins.append(x)
            
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        #if self.stack:
        
        if self.mins[-1] == self.top():
            self.mins.pop()
            
        return self.stack.pop()
        #else:
        #    return None

    def top(self):
        """
        :rtype: int
        """
        #if self.stack:
        return self.stack[-1]
        #else:
        #    return None
        
        

    def getMin(self):
        """
        :rtype: int
        """
        #if self.stack:
        return self.mins[-1]
        #else:
        #    return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
