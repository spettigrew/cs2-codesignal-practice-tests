"""
Suppose there is a circle. There are N petrol pumps on that circle. Petrol pumps are numbered 0 to (N - 1) (both inclusive). You have two pieces of information corresponding to each of the petrol pump: (1) the amount of petrol that particular petrol pump will give, and (2) the distance from that petrol pump to the next petrol pump.

Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps. Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop at each of the petrol pumps. The truck will move one kilometer for each litre of the petrol.

Input Format

The first line will contain the value of N.
The next N lines will contain a pair of integers each, i.e. the amount of petrol that petrol pump will give and the distance between that petrol pump and the next petrol pump.

Constraints:
1 <= N <= 10^5
1 <= amount of petrol, distance <= 10^9

Output Format

An integer which will be the smallest index of the petrol pump from which we can start the tour.

Sample Input

3
1 5
10 3
3 4
Sample Output

1
Explanation

We can start the tour from the second petrol pump.
"""

#!/bin/python3

import os
import sys

#
# Complete the truckTour function below.
#
def truckTour(petrolpumps):
    #
    # Write your code here.
    #
    # answer the question, can we make it around the circle starting at a given index
    # first thing we do when we get to a pump:
        # take all the petrol available
    # second -> try to go to the next pump:
        # if our current is > distance, then we can make it there
    # travel to the next one:
        # increment our index, subtract the distance from current
    
    # if we make it back to our starting point, then we can answer true

    start = 0
    current = 0
    petrol = 0

    while start <= len(petrolpumps):
        petrol += petrolpumps[current][0]
        petrol -= petrolpumps[current][1]
        if petrol < 0:
            # we didn't make it to the next one
            start = current + 1
            current = start
            petrol = 0
            continue
        
        current = (current + 1) % len(petrolpumps)
        
        # OR
        # current += 1
        # if current >= len(petrolpumps):
        #     current = 0

        if current == start:
            return start
    return None

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        n = int(input())

        petrolpumps = []

        for _ in range(n):
            petrolpumps.append(list(map(int, input().rstrip().split())))

        result = truckTour(petrolpumps)

        fptr.write(str(result) + '\n')

        fptr.close()
