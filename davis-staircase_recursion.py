"""
Davis has a number of staircases in his house and he likes to climb each staircase 1, 2, or 3 steps at a time. Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.

Given the respective heights for each of the  staircases in his house, find and print the number of ways he can climb each staircase, module 10^10 + 7 on a new line.

For example, there is s=1 staircase in the house that is n=5 steps high. Davis can step on the following sequences of steps:

1 1 1 1 1
1 1 1 2
1 1 2 1 
1 2 1 1
2 1 1 1
1 2 2
2 2 1
2 1 2
1 1 3
1 3 1
3 1 1
2 3
3 2
There are 13 possible ways he can take these 5 steps. 

Function Description

Complete the stepPerms function in the editor below. It should recursively calculate and return the integer number of ways Davis can climb the staircase, modulo 10000000007.

stepPerms has the following parameter(s):

n: an integer, the number of stairs in the staircase
Input Format

The first line contains a single integer, , the number of staircases in his house.
Each of the following  lines contains a single integer, , the height of staircase .

Constraints
1 <= s <=5
1 <= n <= 36

Subtasks
1 <= n <= 20 for 50% of the maximum score.
Output Format

For each staircase, return the number of ways Davis can climb it as an integer.

Sample Input

3
1
3
7
Sample Output

1
4
44
Explanation

Let's calculate the number of ways of climbing the first two of the Davis'  staircases:

The first staircase only has  step, so there is only one way for him to climb it (i.e., by jumping  step). Thus, we print  on a new line.
The second staircase has  steps and he can climb it in any of the four following ways:
1. 1->1>1
2. 1->2
3. 2->1
4. 3
Thus, we print  on a new line.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
# def stepPerms(n):   # Time Complexity - O(n^3)
#     # if we hit 0
#     if n == 0:
#         # return 1 - at least one way to go up the stairs
#         return -1
#     # if we get below 0
#     if n < 0:
#         # return 0 - no possibilites
#         return 0
        

#     # we try 1, 2, or 3 step combinations (times) call the function recursively for n-1, n-2, n-3)
#     return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
#     # add the results together.
    
# n = 44

# print(stepPerms(n))

# --------- Memoization - increase time complexity -----------
# Memoization - caching the results of a function call
def stepPerms(n):   # Time complexity - O(n) - linear
    memo = {}
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2

    for i in range(3 + n+1):
        # without the third memo - this is similar to a fib challenge
        memo[i] = memo[i-1] + memo[1-2] + memo[1-3]
    return memo[n]

# ------------ Recursion --------------------

# create a global memoization variable - creates a valid cache
memo = {}

def stepPerms(n): 
    #setup memo
    memo = {}
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    # call recursive version - every stair will get a memo assigned to it
    stepPerms(n, memo)

# ------------- Another Memoization approach -----------------
# global dict of nmber of steps. Set up base values
memo = {0: 1, 1: 1, 2: 2,}

def stepPerms(n):    # O(n)
    if n not in memo:
        memo[n] = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
    return memo[n]

    # if __name__ == '__main__':
    #     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #     s = int(input())

    #     for s_itr in range(s):
    #         n = int(input())

    #         res = stepPerms(n)

    #         fptr.write(str(res) + '\n')

    #     fptr.close()
