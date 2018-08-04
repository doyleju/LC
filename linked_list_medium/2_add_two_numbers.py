class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # 76p
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        num1 = num2 = 0
        factor = 1
        
        curr1 = l1
        curr2 = l2
        
        while curr1 or curr2:
            try:
                num1 += curr1.val * factor
                curr1 = curr1.next
            except:
                pass
                
            try:
                num2 += curr2.val * factor
                curr2 = curr2.next
            except:
                pass
                
            factor *= 10
            
        sum_ = num1 + num2
        
        sum_string = str(sum_)[::-1]
        sum_head = ListNode(sum_string[0])
        current = sum_head
        
        len_sum_string = len(sum_string)
        for char in range(1, len_sum_string):
            current.next = ListNode(sum_string[char])
            current = current.next
            
        return sum_head
