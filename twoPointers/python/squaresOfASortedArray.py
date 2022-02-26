# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# !Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# ?Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# !Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

class Solution:
	def sortedSquares(self, nums):
		start, end = 0, len(nums) - 1
		idx = end
		result = [0]*len(nums) 
		
		while end > -1 and idx > -1:
			if abs(nums[start]) > abs(nums[end]):
					result[idx] = nums[start]**2
					start +=1
			else:
					result[idx] = nums[end]**2
					end -=1
			idx -= 1
				
		return result
								