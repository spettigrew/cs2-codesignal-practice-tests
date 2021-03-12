"""
Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.

Example
 k = 1
 arr = [1,2,3,4]

There are three values that differ by k = 1: 2-1 = 1, 3-2 = 1, and 4-3 = 1. Return 3.

Function Description

Complete the pairs function below.

pairs has the following parameter(s):

int k: an integer, the target difference
int arr[n]: an array of integers
Returns

int: the number of pairs that satisfy the criterion
Input Format

The first line contains two space-separated integers n and k, the size of arr and the target value.
The second line contains n space-separated integers of the array arr.

Constraints

2 <= n < = 10^5
0  < k < 10^9
0 < arr[i] < 2^31 -1

each integer arr[i] will be unique
Sample Input

STDIN       Function
-----       --------
5 2         arr[] size n = 5, k =2
1 5 3 4 2   arr = [1, 5, 3, 4, 2]
Sample Output

3
Explanation

There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1]. .
"""

def pairs(k, arr):
    #O(n)
    # we can use a hash table
    # loop over our array and create a hash table
    s = set(arr)
    counter = 0
    #loop over our array
    for val in arr:
        # arr[i] +/- k = what we're looking for
    # use 'i' as a numbered index, not as an element or value
        if val + k in s:
            counter += 1
        # k = what we're looking for - arr[i]
        # check if this value is in our hash table
            # if so, then increment our counter
    
    return counter

def pairs2(k, arr):

    # SORTING => O(n logn)
    # TWO POINTER APPROACH

    # initiate a counter, set it to 0
    arr.sort()
    count = 0
    i,j = 0,1
    # sort our array
    # two pointers, the while loop to check pointers is less than the array. (pointers still in bounds)
    while j < len(arr):
        diff = arr[j] - arr[i]
        if diff == k:
            count += 1
            j += 1
        elif diff > k: 
            i += 1
        elif diff < k: 
            j += 1
        return count

        # subtract the second value from first
            # if value is = k the increment counter
                # increment our pointer
            # if the value is less than
                # then increment the second pointer
            # compare pointers again
            # if difference is < or > than k, increment by 1
            # if value is greater than
                # increment our first pointer
    
    # return the counter
    

print(pairs(1, [1,2,3,4]))