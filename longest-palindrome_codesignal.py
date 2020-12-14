"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2
 

Constraints:

1 <= s.length <= 2000
s consits of lower-case and/or upper-case English letters only.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
     # Get the frequencies of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        # Palindrome consist of even occurences (or frequency) of characters,
        # and at most one additional character (if the length of palindrome is odd).
        # - Add all the characters with even frequencies.
        # - and the chars with odd frequencies, 
        #   subtract 1 from its frequency to make it even, then add
        longest = 0
        for char in freq:
            longest += freq[char]
            if freq[char] % 2 != 0:
                longest -= 1
        # - longest would be even at the end (palindrome length)
        # - longest shorter than length of s implies,
        #   we can add one more character in the middle of the
        #   previous palindrome to still make a valid palindrome.
        if len(s) > longest:
            return longest + 1
        # if length of s is the same as longest,
        # then s itself is a palindrome.
        # Note: length of s can't be less than longest
        return len(s)

# ------------------ Google -----------------------
"""
def get_longest_palindromes(string):
    N = len(string)
    ans = []

    for l in range(N, 0, -1):
        found  = False
        for s in range(N-l+1):
            target = string[s:s+1]
            if target == target[::-1]:
                ans.append(string[s:s+1])
                found = True
        if found:
            break
    return ans if string else [""]
"""