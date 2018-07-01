class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
               
        """
        #1 95p
        carry = 0
        current = len(digits) - 1
        
        while current >= 0:
            if digits[current] == 9:
                carry = 1
                digits[current] = 0
                current -= 1
            elif digits[current] < 9:
                carry = 0
                digits[current] += 1
                return digits
            
        if carry == 1:
            digits.insert(0,carry)
            
        return digits
        
        
        #2 95p
        new_digits = []
        int_number = int(''.join(map(str, digits)))
        int_number += 1
        for digit in str(int_number):
            new_digits.append(int(digit))
        return new_digits
        """
    
        #3 95p
        int_number = 0
        length = len(digits)
        index = 0
        new_digits = []
        
        while index < length:
            int_number += digits[length -1 -index] * (10 ** index)
            index += 1
        
        int_number += 1
        
        for digit in str(int_number):
            new_digits.append(int(digit))
        return new_digits
