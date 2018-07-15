# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        #1 40p
        current = head
        count = 1
        
        while current.next:
            count +=1
            current = current.next
            
        current = head
        new_count = 1
        
        if count == n:
            prev_head = head
            head = head.next
            prev_head.next = None
            #ret_node = prev_head
        else:
            while new_count + n < count:
                current = current.next
                new_count += 1
            ret_node = current.next
            current.next = current.next.next
            
        return head
        """
        
        #2 82p
        slow = head
        fast = head
        
        while n > 0:
            fast = fast.next
            n -= 1
            
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return head
