# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        #1 5p
        
        list_nums = list()
        
        current = head
        count = 0
        
        while current:
            list_nums.append(current.val)
            current = current.next
            count += 1
            
        while count > 1:
            if list_nums.pop(0) != list_nums.pop(-1):
                return False
            
            count -= 2
            
        return True
        """
        
        #2
        
        if not head:
            return True
        
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        slow = head
        slow_n = slow.next
        fast = head.next
        
        while fast:
            slow.next = prev
            prev = slow
            slow = slow_n
            slow_n = slow.next
            
            try:
                fast = fast.next.next
            except:
                fast = fast.next
                
        while slow_n:
            if slow_n.val != prev.val:
                return False
            
            prev = prev.next
            slow_n = slow_n.next
            
        return True
