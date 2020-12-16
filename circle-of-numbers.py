"""
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).
Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.
Example
For n = 10 and firstNumber = 2, the output should be
circleOfNumbers(n, firstNumber) = 7.
Input/Output
[execution time limit] 4 seconds (py3)
[input] integer n
A positive even integer.
Guaranteed constraints:
4 ≤ n ≤ 20.
[input] integer firstNumber
Guaranteed constraints:
0 ≤ firstNumber ≤ n - 1.
[output] integer
Input:
n: 10
firstNumber: 2
Expected Output:
7
Input:
n: 10
firstNumber: 7
Expected Output:
2
nput:
n: 4
firstNumber: 1
Expected Output:
3
Input:
n: 6
firstNumber: 3
Expected Output:
0
Input:
n: 18
firstNumber: 6
Expected Output:
15
Input:
n: 12
firstNumber: 10
Expected Output:
4
"""

def circleOfNumbers(n, firstNumber):
    grouping = n // 2
    target = 0
    if firstNumber >= grouping:
        target = firstNumber - grouping
    else:
        target = firstNumber + grouping
    return target

# ---------- Alternate solution -------------->>>
# def circleOfNumbers(n, firstNumber):
#     # find nums that are direct lines to the number across from it
    
#     # n // 2 + fNum and return fNum
#     # iterate through fNum and check n is greater than or equal to divisor of two
#     if firstNumber >= n // 2:
#         return firstNumber - n // 2
#     return n // 2 + firstNumber

