# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        """
        #1 4p
        current = node
        
        while current.next:
            next_node = current.next
            current.val = next_node.val
            prev = current
            current = next_node
            
        prev.next = None
        """
        
        #2 40p
        node.val = node.next.val
        node.next = node.next.next
