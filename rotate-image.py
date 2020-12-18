"""
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 100,
a[i].length = a.length,
1 ≤ a[i][j] ≤ 104.

[output] array.array.integer
"""

def rotateImage(a):
    """
    Rotate the image 90 degrees clockwise
    a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
    the output should be

    rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
    """
    # initialized the length of a set at 0
    length = len(a[0])
    # iterate through the length // 2
    for idx1 in range(length // 2):
        print(f'idx1, {idx1}')
        # starting from idx1, iterate (num3) over length idx1 -1 -  (should get 1)
        for idx2 in range(idx1, length - idx1 -1):
            print(f'idx2, {idx2}') 
            # initialize a placeholder  
            holder = a[idx1][idx2]
            print(f'holder, {holder}')
            # replace the item at the cur_index of  a[idx1][idx2], with the item 90 degrees before              it
            a[idx1][idx2] = a[length -1 -idx2][idx1]
            # replace the item moved with the item 90 degrees before it
            a[length -1 -idx2][idx1] = a[length -1 -idx1][length -1 - idx2]
             # replace the item moved with the item 90 degrees before it
            a[length -1 -idx1][length -1 - idx2] = a[idx2][length -1 - idx1]
             # replace the item moved with the item 90 degrees before it, which is the holder
            a[idx2][length -1 - idx1] = holder
    return a
