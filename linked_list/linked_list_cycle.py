# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        #1 Failed 2 test cases - timeout
        nodes = []
        current = head
        
        while current:
            if current in nodes:
                return True
            
            nodes.append(current)
            current = current.next
            
        return False
        """
        
        #2 97p
        
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while fast:
            if slow is fast:
                return True
            
            slow = slow.next
            
            try:
                fast = fast.next.next
            except:
                fast = fast.next
                
        return False
