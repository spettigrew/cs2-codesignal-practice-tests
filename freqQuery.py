"""
You are given q queries. Each query is of the form two integers described below:
- 1 x: Insert x in your data structure.
- 2 y: Delete one occurence of y from your data structure, if present.
- 3 z: Check if any integer is present whose frequency is exactly x. If yes, print 1 else 0.

The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation, and queries[i][1]  contains the data element. For example, you are given array queries = [(1,1), (2,2)(3,2),(1,1),(1,1),(2,1),(3,2)]. The results of each operation are:

Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1
Return an array with the output: [01].

Function Description

Complete the freqQuery function in the editor below. It must return an array of integers where each element is a 1 if there is at least one element value with the queried number of occurrences in the current array, or 0 if there is not.

freqQuery has the following parameter(s):

queries: a 2-d array of integers
Input Format

The first line contains of an integer q, the number of queries.
Each of the next q lines contains two integers denoting the 2-d array queries.

Constraints
1 <= q <= 10^5
1 <= x,y,z <= 10^9
All queries[i][0] == {1,2,3}
i <= queries[i][1] <= 10^9

Output Format

Return an integer array consisting of all the outputs of queries of type 3.

Sample Input 0

8
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2
Sample Output 0

0
1
Explanation 0

For the first query of type 3, there is no integer whose frequency is  2(array = [5,6]). So answer is 0.
For the second query of type 3, there are two integers in array = [6,10,10,6] whose frequency is 2 (integers = 6 and 10). So, the answer is 1.

Sample Input 1

4
3 4
2 1003
1 16
3 1
Sample Output 1

0
1
Explanation 1

For the first query of type 3, there is no integer of frequency 4. The answer is 0. For the second query of type 3, there is one integer, 16 of frequency 1 so the answer is 1.

Sample Input 2

10
1 3
2 3
3 2
1 4
1 5
1 5
1 4
3 2
2 4
3 2
Sample Output 2

0
1
1
Explanation 2

When the first output query is run, the array is empty. We insert two 4's and two 5's before the second output query, arr = [4,5,5,4] so there are two instances of elements occurring twice. We delete a 4 and run the same query. Now only the instances of 5 satisfy the query.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):

    valueFreq = Counter()
    freqCount = Counter()

# dictionary
# key -> value
# the added element -> frequency of that value
# use a counter data structure?
# make another dictionary:
# key -> value
# frequency -> [values that occur]

    # keep track of our answer = []
    answer = []
    # loop through each query:
    for query in queries:
        if query[0] == 1:
            freqCount[valueFreq[query[1]]] -= 1
            valueFreq[query[1]] += 1
            freqCount[valueFreq[query[1]]] += 1

        elif query[0] == 2:
            if valueFreq[query[1]] > 0:
                freqCount[valueFreq[query[1]]] -= 1
                valueFreq[query[1]] -= 1
                freqCount[valueFreq[query[1]]] += 1
        else:
            if freqCount[query[1]] > 0:
                answer.append(1)
            else:
                answer.append(0)
        # check for the [0] element and what it is
        #1
            # add the [1] element to our data structure
            # OR increment the count
            # remove it from it's prev place in the second dict, and put it in the next one
        #2 
            #decrement the count, if it doesn;t exist, no-op
        #3 
            # check your data structure if any element occurs x times
            # loop through all the values to see if any of them match x
            # if so, then add a 1 to our answer, if not, add 0
    return answer
    # {
    #     1: [1,2,3,4,5,6,7,8,9],
    #     2: [10,11,12,]
    # }

    # val_freq = {}   

    valueFreq = Counter()
    print(valueFreq["nonexistent"])
    print(valueFreq)


    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        q = int(input().strip())

        queries = []

        for _ in range(q):
            queries.append(list(map(int, input().rstrip().split())))

        ans = freqQuery(queries)

        fptr.write('\n'.join(map(str, ans)))
        fptr.write('\n')

        fptr.close()
