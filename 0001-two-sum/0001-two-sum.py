class Solution(object):
    def twoSum(self, nums, target):
        
	for i, n in enumerate(nums):
		if target - n in nums and i != nums.index(target - n):
			return i, nums.index(target - n)