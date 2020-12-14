"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        results = []
        # put the lowercase char into an array
        for char in s:
            if char.isalpha() or char.isnumeric():
                results.append(char.lower())
        # reverse the array
        res = results[::-1]
        # if equals, itself
        if res == results:
            #return boolean
            return True
        return False