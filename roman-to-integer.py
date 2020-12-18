"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
# if you need the index, do a range loop. If you need the value, do a for/in loop. If you need both, do an enumerate (returns index, and value)



class Solution:
    def romanToInt(self, roman):
        numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}
#  init i as our starting index
        i = 0
        # init num to hold the resulting addition of the found roman numerals
        num = 0
        # iterate the string
        while i < len(roman):
            #  if there are 2 chars to check and they are both in numerals
            if i + 1 < len(roman) and roman[i:i + 2] in numerals:
                # add the integer version of the found 2 character roman numeral to
                # the num var
                num += numerals[roman[i:i + 2]]
                # increment counter by 2 since we found a 2 character roman numeral
                i += 2
            else:
                # add the integer version of the found roman numeral to the num var
                num += numerals[roman[i]]
                # increment counter by 1 since we found a single character roman
                # numeral
                i += 1
        return num
                
                
                
