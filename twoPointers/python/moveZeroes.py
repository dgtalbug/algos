# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# !Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# !Example 2:

# Input: nums = [0]
# Output: [0]

class Solution(object):
	def moveZeroes(self, nums):
		start, end, count = 0, len(nums) - 1, 0
		while start <= end:
			if nums[start] != 0:
						nums[count], nums[start] = nums[start], nums[count]
						count +=1
			start +=1

