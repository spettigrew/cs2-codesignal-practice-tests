"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # set numbers to an empty int
        
        # num_dict = {}
        
        # for i in range(len(nums)):
        #     num_dict[nums[i]] = i
            
        # for i in range(len(nums)):
        #     cur_num = nums[i]
        #     # if target - cur_num is in the dict, check for num in the index
        #     complement = target - cur_num
            
        #     if complement in num_dict and i != num_dict[complement]:
        #         return [i, num_dict[complement]]
        
# complement is the number that will add to the num to equal the target. Or target - cur_num = complement.

# -------------- you tube solution ----------------
        dic = {}
        for i, num in  enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                diff = target - num
                dic[diff] = i

# --------------- NON working code ----------------->>>>>>>> 
        # new_num = {}
        
        # for i in range(len(nums)):
        #     if target - nums[i] in new_num:
        #         return [new_num[target -nums[i]], i] 
        #     else:
        #         new_num[nums[i]] = i
        #     return new_num

# Wrong Answer
# Runtime: 40 ms
# Your input
# [2,7,11,15]
# 9
# Output
# [2]
# Expected
# [0,1]