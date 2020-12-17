"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
"""

class Solution:     # runtime error
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign

        # Remove leading zero in the reversed integer
        while x:
            if x % 10 == 0:
                x /= 10
            else:
                break

        # string manipulation
        x = str(x)
        lst = list(x)  # list('234') returns ['2', '3', '4']
        lst.reverse()
        x = "".join(lst)
        x = int(x)
        return sign*x 