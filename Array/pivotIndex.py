'''
Source : https://leetcode.com/problems/find-pivot-index/
Author : Yuan Wang
Date   : 2018-06-13

/**********************************************************************************
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the 
index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, 
you should return the left-most pivot index.

Example 1:
Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of 
numbers to the right of index 3.
Also, 3 is the first index where this occurs.

Example 2:
Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
**********************************************************************************/
'''

#Time complexity:O(n), Space complexity:O(1)
def pivotIndex(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	part1=0
	part2=sum(nums)
	for i,num in enumerate(nums):  #enumerate is faster than range when using index 
								   #to locate an element
		part2-=num
		if part1 == part2:
			return i
		part1+=num
	return -1

nums=[1, 7, 3, 6, 5, 6]
print(pivotIndex(nums))