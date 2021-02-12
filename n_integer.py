"""
This is a demo task.
Write a function:
def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A):
    # write your code in Python 3.6
    # initiate a counter to keep track of numbers hit
    count = 1
    # if there is a match, return True
    found_match = True
    # iterate through the matched integers
    while found_match == True:
        # if match is true in the count
        if count in A:
            # count the integer
            count += 1
        # otherwise
        else:
            # there is no match, return False 
            found_match = False
            # return the count 
            return count