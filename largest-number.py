"""
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
largestNumber(n) = 99.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 9.

[output] integer

The largest integer of length n.
"""

def largestNumber(n):
    # number of n == how many nines will be in the output
    # initliaze output to be a string of 9 to be the amount of digits
    output = "9"
    # print(n*output)
    #initialize result to n(2) mulitiplied by the output (string of 9)
    result = n * output
    # return  - casting result back to integer
    return int(result)
    
    
    