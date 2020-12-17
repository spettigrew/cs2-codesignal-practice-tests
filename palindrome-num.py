"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
 

Constraints:

-231 <= x <= 231 - 1
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is negative, make it positive 
        if (x < 0): 
            x = (-x); 

        # Create a separate copy of x, so that modifications made to address dupNum don't change the input number. 
        dupNum = (x); # *dupNum = x

        return (x, dupNum)

        if x < 0:
            return False
        p, res = x, 0
        while p:
            res = res * 10 + p % 10
            p /= 10
            res == x
            return True
    
