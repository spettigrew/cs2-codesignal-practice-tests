"""
Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
Example 2:

Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
Example 3:

Input: A = "aa", B = "aa"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Constraints:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist of lowercase letters.
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        # check if strings A and B has at least two characters - if not return False
        if len(A) <= 1 and len(B) <= 1:
            return False
        # iterate through string A
        for i in range(len(A)):
            # initialize a placeholder for the swap
            for j in range(len(A)):
                new_i = ""
                A_copy = list(A)
                if i != j:
                    new_i =  A_copy[j]
                    A_copy[j] = A_copy[i]
                    A_copy[i] = new_i
                    print('A',''.join(A_copy))
                    print('B', B)
                    if ''.join(A_copy) == B:
                        return True
        return False
