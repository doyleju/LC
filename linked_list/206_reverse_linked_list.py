# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head, prev=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #1 75p
        if not head:
            return head
        
        if not head.next:
            return head
        
        if not head.next.next:
            current = head
            head.next.next = head
            head = head.next
            current.next = None
            return head
        
        prev = head
        current = head.next
        next_node = head.next.next
        prev.next = None
        
        while current:
            current.next = prev
            prev = current
            current = next_node
            if next_node:
                next_node = next_node.next
                
        return prev
    
        #2 75p
        current = head
        
        while current:
            head = head.next
            current.next = prev
            current, prev = head, current
            
        return prev
        
        """
        #3 Recursive 15p
        if not head:
            return prev
        
        current = head
        head = head.next
        current.next = prev
        
        return self.reverseList(head, current)
        
        """
