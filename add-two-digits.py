"""
You are given a two-digit integer n. Return the sum of its digits.

Example

For n = 29, the output should be
addTwoDigits(n) = 11.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive two-digit integer.

Guaranteed constraints:
10 ≤ n ≤ 99.

[output] integer

The sum of the first and second digits of the input number.
"""

def addTwoDigits(n):
    # add the two digits to return the sum. 
    
    # change n into a string = casting
    # initialize num to string of n
    num = str(n)
    #  print(type(num)) # now a string, as it has been assigned to a string
    
    # print(num[0], num[1])
    
    return int(num[0]) + int(num[1])
