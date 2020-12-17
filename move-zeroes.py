"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
# O(n^2)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # U - keep order of nums and move 0's to the end
        # Plan - Find all 0's, remove them, add them to the end
        # P2 - Sorting - nums bigger than 0 (won't put in asc order)
        # P3 - shift non-0 nums to the left (or shift 0's to the right)no removing, just shift 0's to the right, until all nums >0 are on the left side
        
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                #scan forward through array until we find non 0 num
                j = i + 1
                while j < len(nums):
                    # keep looping until we find non-0 num, break
                    if nums[j] != 0:
                        break
                    j += 1
                if j >= len(nums):
                    # the inner loop will see all zeroes
                    return
                # now swap values of i and j
                nums [i] = nums[j]
                nums[j] = 0
            i += 1