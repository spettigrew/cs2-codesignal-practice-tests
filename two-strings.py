"""
Given two strings, determine if they share a common substring. A substring may be as small as one character.

Example
s1 = 'and'
s2 = 'art'

These share the common substring a.
s1 = 'be'
s2 = 'cat'

These do not share a substring.

Function Description

Complete the function twoStrings in the editor below.

twoStrings has the following parameter(s):

string s1: a string
string s2: another string
Returns

string: either YES or NO
Input Format

The first line contains a single integer p, the number of test cases.

The following p pairs of lines are as follows:

The first line contains string s1.
The second line contains string s2.
Constraints

s1 and s2 consist of characters in the range ascii[a-z].
1 <= p <= 10
1 <= |s1|, |s2| <= 10^5

Output Format

For each pair of strings, return YES or NO.

Sample Input

2
hello
world
hi
world
Sample Output

YES
NO
Explanation

We have p = 2 pairs to check:

1. s1 = 'hello',s2 = 'world'. The substrings 'o' and 'l' are common to both strings.
2. a = 'hi',b = 'world'. s1 and s2 share no common substrings.

"""
# Having to repeatedly look for something, use a hash table (or a dictionary (key/value pair) or a set(sets only have keys, no values)). Looking a single substring between the two strings, use a hash table.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
# any substring are letters available in both strings.
def twoStrings(s1, s2):

    # O(n^2) = Brute force - iterate through s1,
    # for each letter, we compare it to each letter in s2
    
    # Do they share a substring? Don't care of how many substrings they share. A single letter can be a substring. 
    # do a nested for loop
    # for letter1 in s1:
    #     for letter2 in s2:

    # OR

    # for i in range(len(s1)):
    #     for j in range(len(s2)):
    
#Memoization - recursion    Big O of O(m+n) - linear
    # take every letter in s2 and add it into a hash table, using a set (key only)
    # O(m) where m = |s2|
    set2 = set(s2)

    # take s1 iterate over s1
    # O(n) where n = |s1|
    for letter in s1:
        # check if the letter exists in our hash table
        # return Yes
        if letter in set2:
            return 'YES'
        # if not, return no (outside of the for loop, so it will not return No every time a letter does not match )
    return 'NO'

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        q = int(input())

        for q_itr in range(q):
            s1 = input()

            s2 = input()

            result = twoStrings(s1, s2)

            fptr.write(result + '\n')

        fptr.close()

print(twoStrings("thing", "thing2"))