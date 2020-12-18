"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string that contains only lowercase English letters.

Guaranteed constraints:
1 ≤ s.length ≤ 105.

[output] char

The first non-repeating character in s, or '_' if there are no characters that do not repeat.
"""

def firstNotRepeatingCharacter(s):
    # U - check for non-repeating chars
    
    # create a set of every chars in the string
    # if the non-repeating chars is there, 
    # iterate over the string
    for i in range(len(s)):
        # if the cur_char is not in the chars to left or the right, then it's non-repeating
        if s[i] not in s[:i] and s[i] not in s[i + 1:]:
        # (+ 1 does not include the current index, ending index is not inclusive)
            return s[i]
    return "_"