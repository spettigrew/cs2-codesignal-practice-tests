/*
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5
 

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even

 */

/**
 * @param {number[]} A
 * @return {number}
 */

const repeatedNTimes = (A) => {
    // find n by getting length of array / 2
    let n = A.length / 2
    // find the number in the Aay repeated n times
    let numCount = {}
    
    for (let i = 0; i< n * 2; i ++) {
        if (!(A[i] in numCount)) {
            numCount[A[i]] = 0
        }
        numCount[A[i]] +=1
    }
    for (const key in numCount) {
        if (numCount[key] === n) {
            return key
        }
    }
};


const A = [1,2,3,3,]
console.log(repeatedNTimes(A))